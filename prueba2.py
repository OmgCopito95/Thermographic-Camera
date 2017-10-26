import serial
import time
import numpy as np

ser = serial.Serial('COM4', 9600, timeout=0)
dato = ser.read(5)

while (dato!=".." and dato!="."):
    if (dato!=".." and dato!="." and dato!=""):
        print dato
        with open("datos.txt", "a") as file:
            file.write("{0}\n".format(dato))
        time.sleep(0.035)
    else:
        dato=ser.read(5)
