# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


filas = 3
columnas = 4

with open("datos.html", "w") as file:
    file.write('<!DOCTYPE html><html><head><meta charset="utf-8"><link type="text/css" rel="stylesheet" href="static/bootstrap/css/custom.css" media="all"></head><body>')

temp = [2,4,8,3],[6,1,7,1],[12,1,2,6.3]
'''[1.5,1,1,1]
   [6,1,2,1]
   [12,1,2,1]'''


plt.imshow(temp, cmap='hot') #Create image with scale colors
plt.colorbar() #Draw color bar
plt.savefig('imagen.png', bbox_inches='tight')
#plt.show()  #Show image 

for i in xrange (0,filas): # i = columnas
    for j in xrange (0,columnas): # j = filas
        print temp[i][j]
        with open("datos.html", "a") as file:
            file.write('<div class="tooltip" style=" border: none; position: absolute; width: 100px; height: 100px; left: {1}px; top:{0}px;"><span class="tooltiptext">{2}°C</span></div>'.format(i*100+58,j*100+62,temp[i][j]))
with open("datos.html", "a") as file:
    file.write('<img src="imagen.png" alt="" /></body></html>') 