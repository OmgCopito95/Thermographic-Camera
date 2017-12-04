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
    
    minimo = 999
    maximo = -999

    ser = serial.Serial('COM3', 9600, timeout=0)
    #Leo el primer dato
    try:
        dato = ser.read(5)
        print dato
    except:
        print('No se pudo leer el dato')
    time.sleep(0.035)
    #time.sleep(0.040)
    #time.sleep(0.1)
    #time.sleep(0.5)

    while ("@" not in dato and dato != "pausa"):
        if (dato != ""):
            try:
                dato = ser.read(5)
                print dato
            except:
                print('No se pudo leer el dato')

            if (dato != '#####' and "@" not in dato and dato != ""):
                #guarda el dato leido en el archivo de texto
                with open("datos.txt", "a") as file:
                    file.write("{0}\n".format(dato))
            else:
                if (dato == '#####'): # avanzo de fila
                    with open("datos.txt", "a") as file:
                        file.write("#####")

            time.sleep(0.035) #mismo tiempo con el cual lee el arduino
            #time.sleep(0.040)
            #time.sleep(0.1) #segundos
            #time.sleep(0.5)
        else: #lee un espacio en blanco
            try:
                dato = ser.read(5)
                print dato
            except:
                print('No se pudo leer el dato')
            time.sleep(0.035)
            #time.sleep(0.040)
            #time.sleep(0.1)
            #time.sleep(0.5)

    #Salio del while por lo tanto finalizo
    if ("@" in dato):
        # Muestro la pagina con el resultado
        print ("finalizo el escaneo")
        ser.close()

def verificar(): # verifica que los valores leidos del puerto serie tengan el formato xx.xx
    with open("datos.txt", "r") as f:
        lineas = f.readlines()
    for i in range(len(lineas)):
        l=lineas[i]
        ultimoDato="" # Dato anterior
        if i>1:
            with open("datosVerificados.txt","r") as g:
                lVerif = g.readlines()
                ultimoDato = lVerif[len(lVerif)-1]
                anteUltimoDato = lVerif[len(lVerif)-2] 
        try:
            # verifica que cumpla con el formato xx.xx siendo x un entero
            if (int(l[:2]) and l[2:3]=="." and int(l[3:5])):
                with open("datosVerificados.txt","a") as f:
                    f.write("{0}".format(l))
            else:
                int("error")
        except:
            with open("datosVerificados.txt","a") as f:
                if (l[:1] == "."): # Si el primer digito es un . 
                    num = l[3:5] + "." + l[1:3] # .1234 ---> 34.12
                    f.write("{0}\n".format(num))
                elif (l[4:5] == "."):
                    num = l[2:4] + "." + l[:2]
                    f.write("{0}\n".format(num))
                if ("#" in lineas[i] and "#" not in ultimoDato):
                    f.write("{0}\n".format("#####"))
                elif(i == 0): # Primer dato
                    f.write("{0}\n".format("00.00"))
                else:
                    if (len(lineas[i])<5 and lineas[i-1]!="#####"):
                        # Si al dato le faltan caracteres, utiliza el anterior
                        f.write("{0}".format(ultimoDato))
                    elif (lineas[i-1]!="#####"): # Si no vino un separador, utiliza el dato anterior
                        f.write("{0}".format(ultimoDato))
                    else: # sino utiliza el anteultimo leido
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


def min_max():
    minimo = 999
    maximo = -999
    with open("datosVerificados.txt", "r") as f:
        lineas = f.readlines()
    #print("minimo" + str(minimo))
    for l in lineas:
        try:
            l=float(l)
            if(l < minimo):
                minimo = l
                print("minimo" + str(minimo))
                with open("temperaturas.txt", "w") as f:
                    f.write("{0}\n{1}\n".format(minimo,maximo))
            elif (l > maximo):
                maximo = l
                with open("temperaturas.txt", "w") as f:
                    f.write("{0}\n{1}\n".format(minimo,maximo))
        except:
            pass
    with open("temperaturas.txt", "a") as f: #guardo un fin en el archivo de temperaturas para habilitar el boton ver Resultado
        f.write("fin")
    

#iniciar()
#leer()
#verificar()
#crearMatriz()
#min_max()