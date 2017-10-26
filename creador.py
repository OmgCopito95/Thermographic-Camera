# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from html_variables import *
import lector_datos


def crear_html_imagen(): # Crea el html con la imagen escaneada.
                         # Recibe como parámetro la matriz con los datos de temperatura escaneados.
    #print "caca"
    filas = 36
    columnas = 179
    m = lector_datos.crearMatriz()
    with open("templates/datos.html", "w") as file:
        file.write('<!DOCTYPE html>{0}<body style="background: none;">'.format(HTML_HEAD))

    #print m
    #plt.imshow(temp, cmap='hot') #Create image with scale colors
    plt.imshow(m, cmap='hot',interpolation='nearest', aspect='auto') #Create image with scale colors
    
    plt.colorbar() #Draw color bar
    plt.savefig('static/images/imagen.png')
    #plt.show()  #Show image 

    '''for i in xrange (0,filas): # i = columnas
        for j in xrange (0,columnas): # j = filas
            print temp[i][j]
            with open("templates/datos.html", "a") as file:
                file.write('<div class="tooltip" style=" border: none; position: absolute; width: 100px; height: 100px; left: {1}px; top:{0}px;"><span class="tooltiptext">{2}°C</span></div>\n'.format(i*100+58,j*100+62,temp[i][j]))
    with open("templates/datos.html", "a") as file:
        file.write('{0}</body></html>'.format(HTML_IMAGEN))'''
    #print filas
    #print columnas
    '''for i in range (0,filas):
        for j in range (0,columnas): 
            #print m[i][j]
            with open("templates/datos.html", "a") as file:
                file.write('<div class="tooltip" style=" border: none; position: absolute; width: 100px; height: 100px; left: {1}px; top:{0}px;"><span class="tooltiptext">{2}°C</span></div>\n'.format(i*30+58,j*30+62,m[i][j]))
    with open("templates/datos.html", "a") as file:
        print "caca"
        file.write('{0}</body></html>'.format(HTML_IMAGEN))'''
    with open("templates/datos.html", "a") as file:
        file.write('{0}</body></html>'.format(HTML_IMAGEN))