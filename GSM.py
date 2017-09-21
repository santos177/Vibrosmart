#!usr/bin/python
#Prueba de conexion con modulo GSM A6 Thinker, para Vibrosmart!
import serial
import time
import RPi.GPIO as RPIO
from math import *
#seteamos el puerto GPIO numero 18
RPIO.setmode(RPIO.BCM)
RPIO.setwarnings(False) 
RPIO.setup(18,RPIO.OUT,initial=RPIO.LOW)
RPIO.setup(23,RPIO.OUT,initial=RPIO.LOW)

class GSM:
    
    def __init__(self):
        self.data = []
    
    def set(self):
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
    

    def off(self):
       print("Apagando el Modulo GSM...")
       time.sleep(3)
       RPIO.output(23,RPIO.LOW)
       RPIO.output(18,RPIO.HIGH)
       time.sleep(0.5)
       RPIO.output(18,RPIO.LOW)


    def call(self,number):
       self.numero = numero 
       port = serial.Serial('/dev/ttyS0',115200, timeout=5)
       print (port.name)
       port.write(b'AT+CPIN?\r')#  preguntamos por el PIN
       time.sleep(0.5)
       respuesta = port.readlines() 
       print(respuesta)
       port.write(b'AT+CREG=?\r')
       time.sleep(0.5)
       respuesta = port.readlines() 
       print(respuesta)
       port.write(b'AT+CREG?\r')
       time.sleep(0.5)
       respuesta = port.readlines() 
       print(respuesta)
       port.write(b'ATD+'+number+';\r')# hacemos una llamada!
       time.sleep(10)
       respuesta = port.readlines() 
       print(respuesta)
       port.write(b'ATH\r')
       respuesta = port.readlines()
       time.sleep(1)
       print(respuesta)


    def sms(self,number,mensaje):
        self.mensaje = mensaje
        self.number = number 
        port = serial.Serial('/dev/ttyS0',115200, timeout=5)
        print (port.name)
        port.write(b'AT+CPIN?\r\n')#  preguntamos por el PIN
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(b'AT+CMGF=?\r\n')# preguntamos por los modos de texto que soporta el GSM
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(b'AT+CMGF=1\r\n')# seteamos el modo de texto
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(b'AT+CSCS="GSM"\r\n')# seteamos el set de caracteres a usar
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(b'AT+CMGS="+'+number+b'"\r\n')# seteamos el destinatario 
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(mensaje+b'\r\n')# escribimos el mensaje
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write("\x1A") # activado para enviar mensajes (codigo ASCII numero 26)
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)

        
    def post(self,datos):
        self.datos = datos
        port = serial.Serial('/dev/ttyS0',115200, timeout=5)
        print (port.name)
        port.write(b'AT+COPS?\r\n')#  preguntamos por las redes presentes
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(b'AT+CGATT=?\r\n')#  preguntamos si el GPRS esta adjunto a la red
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(b'AT+CGATT=1\r\n')#  nos adjuntamos de todas formas
        time.sleep(0.5)
        respuesta = port.readlines() 
        print(respuesta)
        port.write(b'AT+CGATT=?\r\n')#  preguntamos si el GPRS esta adjunto a la red
        time.sleep(0.5)
        respuesta = port.readlines() 
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
        port.write(b'Content-Length: 8\r\n\r\n')
        time.sleep(0.5)
        respuesta = port.readlines()
        print(respuesta)
        port.write(b'key='+datos)
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


numero = "56990250523"
mensaje ="Esta es solo una prueba Diegote"
datos = "Muse" 
gsm = GSM()
gsm.set()
gsm.post(datos)
gsm.off()


