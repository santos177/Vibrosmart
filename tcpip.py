#!usr/bin/python
#Prueba con comandos TCP IP en modulo GSM A6 Thinker, para Vibrosmart!
import serial
import time
import RPi.GPIO as RPIO
from math import *
#seteamos el puerto GPIO numero 18
RPIO.setmode(RPIO.BCM)
RPIO.setwarnings(False) 
RPIO.setup(18,RPIO.OUT,initial=RPIO.LOW)
RPIO.setup(23,RPIO.OUT,initial=RPIO.LOW)
#utilizamos el puerto serial ttySO
time.sleep(3)
RPIO.output(23,RPIO.HIGH)
time.sleep(7)
print("Reseteando Modulo GSM...")
time.sleep(3)
RPIO.output(18,RPIO.HIGH)
time.sleep(0.5)
RPIO.output(18,RPIO.LOW)
time.sleep(20)
print("Iniciando modulo GSM...")
port = serial.Serial('/dev/ttyS0',115200, timeout=10)
print (port.name)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT\r\n')  # Iniciamos la comunicacion
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
string = "thecure"
port = serial.Serial('/dev/ttyS0',115200, timeout=5)
print (port.name)
port.write(b'AT\r')  # Iniciamos la comunicacion  (\r\n significa ENTER )
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CREG=?\r\n')# preguntamos si la sim esta registrada
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write(b'ATI\r\n')# preguntamos por la marca
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CGMM\r\n')# preguntamos por la info del modelo
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSTATUS\r\n')#  preguntamos por el status TCP IP
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+COPS?\r\n')#  preguntamos por las redes presentes
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CGATT?\r\n')#  preguntamos si el GPRS esta adjunto a la red
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CGATT=1\r\n')#  nos adjuntamos de todas formas
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CGATT?\r\n')#  preguntamos si el GPRS esta adjunto a la red
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSTATUS\r\n')# el status de la IP
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CGDCONT=1,"IP","imovil.entelpcs.cl"\r\n')#  ponemos las credenciales que necesitamos para ingresar (EL PDP context y el apn )
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSTATUS\r\n')# el status de la IP
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CGACT=1,1\r\n')#  activamos el PDP context!
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSTATUS\r\n')# el status de la IP
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIFSR\r\n')# pedimos la IP
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSTATUS\r\n')# el status de la IP
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSTART="TCP","186.64.118.130",80\r\n')#  Nos conectamos a chilealoha!!!!
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSEND\r\n')# Enviando datos a chilealoha!!!!
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'POST /ebox/raspberry.php HTTP/1.1\r\n')# escribimos el mensaje
time.sleep(0.5)
respuesta = port.readlines()
print(respuesta)
port.write(b'HOST: chilealoha.cl\r\n')
time.sleep(0.5)
respuesta = port.readlines()
print(respuesta)
port.write(b'User-Agent: curl/7.45.0\r\n')
time.sleep(0.5)
respuesta = port.readlines()
print(respuesta)
port.write(b'Accept: */*\r\n')
time.sleep(0.5)
respuesta = port.readlines()
print(respuesta)
port.write(b'Content-Type: application/x-www-form-urlencoded\r\n')
time.sleep(0.5)
respuesta = port.readlines()
print(respuesta)
port.write(b'Content-Length: 11\r\n\r\n')
time.sleep(0.5)
respuesta = port.readlines()
print(respuesta)
port.write(b'key='+string)
time.sleep(0.5)
respuesta = port.readlines()
print(respuesta)
port.write("\x1A") # activado para enviar mensajes (codigo ASCII numero 26)
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPCLOSE\r\n')# cerramos la conexion con chilealoha
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSHUT\r\n')# cerrando conexion wireless
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
print("Apagando el Modulo GSM...")
time.sleep(3)
RPIO.output(23,RPIO.LOW)
RPIO.output(18,RPIO.HIGH)
time.sleep(0.5)
RPIO.output(18,RPIO.LOW)

"""
port.write(b'AT+CIPSTATUS\r\n')# el status de la IP
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CSTT="imovil.entelpcs.cl","entelpcs","entelpcs"\r\n')#  ponemos user y password
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CIPSTART="TCP","64.233.190.147",80\r\n')#  Nos conectamos a GOOGLE!!!!
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)

"""
