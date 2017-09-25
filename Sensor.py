#!usr/bin/python
#Clase I2C para Vibrosmart!

from smbus import SMBus
import time
from math import *
import numpy as np
import pylab as pl
import timeit

class Sensor:

    def __init__(self):
        self.data = []

    def read(self,points,axis):       # points: numero de muestras, axis: eje "x","y "o "z".
        self.points = points
        self.axis = axis
        bus = SMBus(1)
        bus.write_byte_data(0x1D, 0x2A, 0x00)
        time.sleep(0.2)
        bus.write_byte_data(0x1D, 0x2A, 0x01)
        time.sleep(0.2)
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
        print( "leyendo...")
        starttime = time.time()

        for i in range(0,points):

              data.append(bus.read_i2c_block_data(0x1D, 0x00,7))

        elapsed = time.time() - starttime
        print(elapsed)

        for a in range(0,points):

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

        if axis == "x":
            return c1
        elif axis == "y":
            return c2
        elif axis == "z":
            return c3
        else:
            print ("Debe ingresar un eje: 'x','y' o 'z'")
        bus.write_byte_data(0x1D, 0x2A, 0x00)
        time.sleep(0.5)
        
    def graph(self,c):    #c: el array con el muestreo
        self.c = c
        print ("Graficando...")
        pl.plot(t,c,'-r')
        pl.show()


# TEST!
sensor = Sensor()
y = sensor.read(10,"y")
sensor.graph(y)


#pl.plot(t,c1)
#w = np.array(c2)
#frec = np.fft.rfft(w,100,-1)     analisis en frecuencia por medio de la FFT
#print frec
