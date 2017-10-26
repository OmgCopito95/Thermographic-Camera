# Lee los datos del puerto serie que genera el sensor en el Arduino
# Genera una matriz con los datos

import serial
import time
import numpy as np


def iniciar():
    with open("datos.txt", "w") as file:
        file.write("")
    with open("datosVerificados.txt", "w") as file:
        file.write("")
    


def leer():
    ser = serial.Serial('COM4', 9600, timeout=0)
    #Leo el primer dato
    try:
        dato = ser.read(5)
        print dato
    except:
        print('No se pudo leer el dato')
    time.sleep(0.035)

    while (dato != "deten" and dato != "pausa"):
        #print ("entro while")
        if (dato != ""):
            #print ("entro if")

            if (columnas < 178 and volver == False):
                columnas=columnas+1
            else:
                if (columnas > 0 and volver == True):
                    columnas = columnas - 1 #comienza a contar de zero de nuevo

            if (columnas == 178):
                volver = True;
            else: 
                if (columnas == 0):
                    volver = False
            try:
                dato = ser.read(5)
                print dato
            #   print len(dato)
            except:
                print('No se pudo leer el dato')
            #Leo el siguiente dato
            #print filas
            #print columnas
            if (dato != '#####' and dato !="deten" and dato!="pausa" and dato != ""):
                with open("datos.txt", "a") as file:
                    file.write("{0}\n".format(dato))
                #matriz[filas][columnas] = float(dato)
            else:
                if (dato == '#####' and filas < 34): # avanzo de fila
                    with open("datos.txt", "a") as file:
                        file.write("#####")
                    filas=filas+1
            #print('Data could not be read')
            time.sleep(0.035) #mismo tiempo con el cual lee el arduino
        else:
            try:
                dato = ser.read(5)
                print dato
            except:
                print('No se pudo leer el dato')
            time.sleep(0.035)

    #Salio del while por lo tanto le llego un finalizo o un detener
    #print("salio del while")

    if (dato == "deten"):
        # Muestro la pagina con el resultado
        print ("finalizo el escaneo")
        ser.close()
    else:
        if (dato == "pausa"):
            print ("Se detuvo el escaneo")
            ser.close()
            # Muestro un cartel diciendo que se detuvo el escaneo y que comience de nuevo

def verificar(): # verifica que los valores leidos del puerto serie tengan el formato xx.xx
    with open("datos.txt", "r") as f:
        lineas = f.readlines()
    for i in range(len(lineas)):
        #print len(lineas)
        l=lineas[i]
        ultimoDato=""
        if i>1:
            with open("datosVerificados.txt","r") as g:
                lVerif = g.readlines()
                ultimoDato = lVerif[len(lVerif)-1]
                anteUltimoDato = lVerif[len(lVerif)-2] 
        try:
            if (int(l[:2]) and l[2:3]=="." and int(l[3:5])):
                with open("datosVerificados.txt","a") as f:
                    f.write("{0}".format(l))
            else:
                int("caca")
        except:
            #guardo el valor anterior para poder interpolar
            #print i
            with open("datosVerificados.txt","a") as f:
                if ("#" in lineas[i] and "#" not in ultimoDato):
                    f.write("{0}\n".format("#####"))
                elif(i == 0):
                    f.write("{0}\n".format("00.00"))
                else:
                    if (len(lineas[i])<5 and lineas[i-1]!="#####"):
                        f.write("{0}".format(ultimoDato))
                    elif (lineas[i-1]!="#####"):
                        f.write("{0}".format(ultimoDato))
                    else:
                        f.write("{0}".format(anteUltimoDato))

def crearMatriz():
    d = (34,179) #filas columnas
    matriz = np.zeros(d) #inicializo la matriz toda en cero
    volver = False
    columnas = -1
    filas = 0

iniciar()
leer()
verificar()