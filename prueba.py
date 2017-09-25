#!usr/bin/python
#Prueba del bus I2C para Vibrosmart!

from smbus import SMBus
import time
from math import *
import numpy as np
import pylab as pl
import timeit
#from smbus import SMBus
# Get I2C bus
bus = SMBus(1)  #utilizamos el bus i2c 1 de la raspberry pi

# MMA8452Q address, en este caso la direccion del dispositivo es 0xd10
# Select Control register, 0x2A(42)
#		0x00(00)	StandBy mode
bus.write_byte_data(0x1D, 0x2A, 0x00) # es necesario verificar el registro de control para el MMA8452Q
time.sleep(0.2)
# MMA8452Q address, 0x1C(28)
# Select Control register, 0x2A(42)
#		0x01(01)	Active mode
bus.write_byte_data(0x1D, 0x2A, 0x01)
time.sleep(0.2)
# MMA8452Q address, 0x1C(28)
# Select Configuration register, 0x0E(14)
#		0x00(00)	Set range to +/- 2g
bus.write_byte_data(0x1D, 0x0E, 0x00)

time.sleep(0.5)
t = []
x1 = []
x2 = []
y1 = []
y2 = []
z1 = []
z2 = []
c1 = []
c2 = []
c3 = []
data = []
strip = [] 
# MMA8452Q address, 0x1D
# Read data back from 0x00(0), 7 bytes
# Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
  # capturamos rapidamente los bytes enviados por el acelerometro
print( "leyendo...")
starttime = time.time()
for i in range(0,10000):

      data.append(bus.read_i2c_block_data(0x1D, 0x00,7))

elapsed = time.time() - starttime
print(elapsed)
for a in range(0,10000):

     strip = data[a]
     x1.append(strip[1])
     x2.append(strip[2])
     xAccl = (x1[a]*256 + x2[a]*16) / 16
     if xAccl > 2047 :
           xAccl -= 4096
     y1.append(strip[3])
     y2.append(strip[4])
     yAccl = (y1[a]*256 + y2[a]*16) / 16
     if yAccl > 2047 :
           yAccl -= 4096
     z1.append(strip[5])
     z2.append(strip[6])
     zAccl = (z1[a]*256 + z2[a]*16) / 16
     if zAccl > 2047 :
           zAccl -= 4096
     t.append(a)
     c1.append(xAccl)
     c2.append(yAccl)
     c3.append(zAccl)

print ("Graficando...")
#pl.plot(t,c1)
#w = np.array(c2)
#frec = np.fft.rfft(w,100,-1)     analisis en frecuencia por medio de la FFT 
#print frec


pl.plot(t,c2,'-r')
#pl.plot(t,c3,'g')

pl.show()
bus.write_byte_data(0x1D, 0x2A, 0x00) 
time.sleep(0.5)
