#!usr/bin/python
#Prueba de conexion con modulo GSM A6 Thinker, para Vibrosmart!
import serial
import time
from math import *
import numpy as np
import pylab as pl
#utilizamos el puerto serial ttySO
mensaje= "mensaje de prueba" 
port = serial.Serial('/dev/ttyS0',115200, timeout=5)
print (port.name)
port.write(b'AT\r')  # Iniciamos la comunicacion
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
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
port.write(b'ATD+56990250523;\r')# hacemos una llamada!
time.sleep(10)
respuesta = port.readlines() 
print(respuesta)
port.write(b'ATH\r')
respuesta = port.readlines()
time.sleep(1)
print(respuesta)
"""
time.sleep(0.5)
port.write(b'AT+CMGS="'+receptor.encode()+b'"\r')# enviamos el mensaje de texto
time.sleep(0.5)
port.write(mensaje.encode()+b'\r')
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(bytes([26]))
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.close()
port.write(b'AT+CMGF=1\r')
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CMGS="'+mensaje.encode()+b'"\r')
time.sleep(0.5)
port.write(bytes([26]))
finally:
time.sleep(0.5)
port.close()
cmd = b'ATZ\r'
cmd1 = b'AT+CMGF=1\r'#en modo de texto
cmd2 = b'AT+CMGS=?\r'#preguntamos que modos usa el gsm
cmd3 = b'+CEER=\r'#preguntamos que modos usa el gsm
#escribimos el comando AT mas ENTER, para que nos responda el modulo GSM con un OK por la terminal
port.write(cmd)
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
"""

