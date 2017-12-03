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
    
    min = 999
    max = -999

    ser = serial.Serial('COM3', 9600, timeout=0)
    #Leo el primer dato
    try:
        dato = ser.read(5)
        print dato
    except:
        print('No se pudo leer el dato')
    time.sleep(0.035)
    #time.sleep(0.1)
    #time.sleep(0.5)

    while (dato != "deten" and dato != "pausa"):
        if (dato != ""):
            try:
                dato = ser.read(5)
                print dato
            except:
                print('No se pudo leer el dato')

            if (dato != '#####' and dato !="deten" and dato!="pausa" and dato != ""):

                #Pregunto si es menor al minimo o mayor al maximo
                min_max(dato,min,max)

                with open("datos.txt", "a") as file:
                    file.write("{0}\n".format(dato))
            else:
                if (dato == '#####'): # avanzo de fila
                    with open("datos.txt", "a") as file:
                        file.write("#####")
            time.sleep(0.035) #mismo tiempo con el cual lee el arduino
            #time.sleep(0.1) #segundos
            #time.sleep(0.5)
        else:
            try:
                dato = ser.read(5)
                print dato
            except:
                print('No se pudo leer el dato')
            time.sleep(0.035)
            #time.sleep(0.1)
            #time.sleep(0.5)

    #Salio del while por lo tanto le llego un finalizo o un detener
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
    matriz = np.full((36,179),20.00) #inicializo la matriz toda en temperatura ambiente
    volver = False
    columnas = 0
    filas = 0
    with open("datosVerificados.txt","r") as f:
        lineas = f.readlines()
        for l in lineas: 
            if ("#####" not in l[:-1]):              
                matriz[filas][columnas] = float(l[:-1])

                if (columnas == 178 and volver==False):
                    volver = True
                    columnas+=1

                if (columnas == 0 and volver==True):
                    volver = False
                    columnas-=1

                if (columnas < 178 and volver == False):
                    columnas=columnas+1
                else:
                    if (columnas > 0 and volver == True):
                        columnas = columnas - 1 #comienza a contar de zero de nuevo
            else:
                filas = filas + 1
    return matriz


def min_max(dato,min,max):
    if(dato < min):
        min = dato
        with open("temperaturas.txt", "w") as file:
            file.write("{0}\n{1}\n".format(min,max))
    elif (dato > max):
        max = dato
        with open("temperaturas.txt", "w") as file:
            file.write("{0}\n{1}\n".format(min,max))

#iniciar()
#leer()
#verificar()
#crearMatriz()