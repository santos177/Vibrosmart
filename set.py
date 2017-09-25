#!usr/bin/python
#Prueba de conexion con modulo GSM A6 Thinker, para Vibrosmart!
import serial
import time
import RPi.GPIO as RPIO
from math import *
import numpy as np
import pylab as pl
#seteamos el puerto GPIO numero 18 , el 18 resetea, el 23 da el PWR
RPIO.setmode(RPIO.BCM)
RPIO.setwarnings(False) 
RPIO.setup(18,RPIO.OUT,initial=RPIO.LOW)
RPIO.setup(23,RPIO.OUT,initial=RPIO.LOW)
print("Encendiendo el Modulo GSM...")
time.sleep(3)
RPIO.output(23,RPIO.HIGH)
time.sleep(7)
print("Reseteando Modulo GSM...")
time.sleep(3)
RPIO.output(18,RPIO.HIGH)
print("HIGH...")
time.sleep(0.5)
RPIO.output(18,RPIO.LOW)
print("LOW...")
time.sleep(20)
#utilizamos el puerto serial ttySO
mensaje= "mensaje de prueba"
print("Iniciando modulo GSM...")
port = serial.Serial('/dev/ttyS0',115200, timeout=10)
print (port.name)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT\r\n')  # Iniciamos la comunicacion
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
print("Apagando el Modulo GSM...")
time.sleep(3)
RPIO.output(23,RPIO.LOW)
RPIO.output(18,RPIO.HIGH)
print("HIGH...")
time.sleep(0.5)
RPIO.output(18,RPIO.LOW)
print("LOW...")

