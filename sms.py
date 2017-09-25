#!usr/bin/python
#Prueba con SMS en modulo GSM A6 Thinker, para Vibrosmart!
import serial
import time
#utilizamos el puerto serial ttySO
mensaje = "mensaje de prueba VC"
receptor ="+56990250523" 
port = serial.Serial('/dev/ttyS0',115200, timeout=5)
print (port.name)
port.write(b'AT\r')  # Iniciamos la comunicacion  (\r\n significa ENTER )
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CPIN?\r\n')#  preguntamos por el PIN
time.sleep(0.5)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CMGF=?\r\n')# preguntamos por los modos de texto que soporta el GSM
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CMGF=1\r\n')# seteamos el modo de texto
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CSCS="GSM"\r\n')# seteamos el set de caracteres a usar
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write(b'AT+CMGS="+56990250523"'+'\r\n')# seteamos el destinatario 
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write(b'respuesta del modulo> Picosan'+'\r\n')# escribimos el mensaje
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
port.write("\x1A") # activado para enviar mensajes (codigo ASCII numero 26)
time.sleep(1)
respuesta = port.readlines() 
print(respuesta)
