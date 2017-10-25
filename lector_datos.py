# Lee los datos del puerto serie que genera el sensor en el Arduino
# Genera una matriz con los datos

import serial
import time
import numpy as np


matriz = []
s = (35,180)
matriz = np.zeros(s)

def leer():
    ser = serial.Serial('COM4', 9600, timeout=0)
    i = 0
    a=0
    #Leo el primer dato
    try:
        dato = ser.read(5)
        print dato
    except ser.SerialTimeoutException:
        print('No se pudo leer el dato')
    time.sleep(0.035)

    while (dato != ".." and dato != "."):
        #Creo matriz con los datos
        try: #Leo el siguiente dato
            dato = ser.read(5)
            print dato
            if (dato == "#####"):
                a=a+1
        except ser.SerialTimeoutException:
            print('Data could not be read')
        time.sleep(0.035) #mismo tiempo con el cual lee el arduino
        i=i+1

    #Salio del while por lo tanto le llego un finalizo o un detener
    print("salio del while")

    if (dato == ".."):
        # Muestro la pagina con el resultado
        print ("finalizo el escaneo")
        ser.close()
    else:
        if (dato == "."):
            print ("Se detuvo el escaneo")
            ser.close()
            
        # Muestro un cartel diciendo que se detuvo el escaneo y que comience de nuevo
    print i
    print a
leer()