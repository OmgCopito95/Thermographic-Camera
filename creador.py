# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from html_variables import *


def crear_html_imagen(): # Crea el html con la imagen escaneada.
                         # Recibe como parámetro la matriz con los datos de temperatura escaneados.
    filas = 3
    columnas = 4

    with open("templates/datos.html", "w") as file:
        file.write('<!DOCTYPE html>{0}<body style="background: none;">'.format(HTML_HEAD))

    

    plt.imshow(temp, cmap='hot') #Create image with scale colors
    plt.colorbar() #Draw color bar
    plt.savefig('static/images/imagen.png', bbox_inches='tight')
    #plt.show()  #Show image 

    for i in xrange (0,filas): # i = columnas
        for j in xrange (0,columnas): # j = filas
            print temp[i][j]
            with open("templates/datos.html", "a") as file:
                file.write('<div class="tooltip" style=" border: none; position: absolute; width: 100px; height: 100px; left: {1}px; top:{0}px;"><span class="tooltiptext">{2}°C</span></div>\n'.format(i*100+58,j*100+62,temp[i][j]))
    with open("templates/datos.html", "a") as file:
        file.write('{0}</body></html>'.format(HTML_IMAGEN)) 