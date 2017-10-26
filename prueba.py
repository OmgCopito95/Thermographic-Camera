import numpy as np
import serial
d = (5,2) #filas columnas
matriz = np.zeros(d) #inicializo la matriz toda en cero
columnas = 0
filas = 0
ser = serial.Serial('COM4', 9600, timeout=0)

try: #Leo el siguiente dato
    dato = ser.read(5)
    print dato
    matriz[0][0]=float(dato)
except:
    print('Data could not be read')
if dato== "":
    print "caca"
