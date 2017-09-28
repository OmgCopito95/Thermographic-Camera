import matplotlib.pyplot as plt
import numpy as np

#Metodo recolectar datos de puerto serie.

filas = 3
columnas = 4

with open("datos.html", "w") as file:
    file.write('<!DOCTYPE html><html><style>.tooltip {position: relative;display: inline-block;border-bottom: 1px dotted black;}.tooltip .tooltiptext {visibility: hidden;width: 120px;background-color: #555;color: #fff;text-align: center;border-radius: 6px;padding: 5px 0;position: absolute;z-index: 1;bottom: 125%;left: 50%;margin-left: -60px;opacity: 0;transition: opacity 1s;}.tooltip .tooltiptext::after {content: "";position: absolute;top: 100%;left: 50%;margin-left: -5px;border-width: 5px;border-style: solid;border-color: #555 transparent transparent transparent;}.tooltip:hover .tooltiptext {visibility: visible;opacity: 1;}</style><head><link type="text/css" rel="stylesheet" href="custom.css" media="all"></head><body>')

temp = [1.5,1,1,1],[6,1,2,1],[12,1,2,1]
'''[1.5,1,1,1]
   [6,1,2,1]
   [12,1,2,1]'''

plt.imshow(temp, cmap='hot') #Create image with scale colors
#plt.colorbar() #Draw color bar
#plt.savefig('imagen.png', bbox_inches='tight')
#plt.show()  #Show image 

for i in xrange (0,filas): # i = columnas
    for j in xrange (0,columnas): # j = filas
        print temp[i][j]
        with open("datos.html", "a") as file:
            file.write('<div class="tooltip" style=" background-color: red; position: absolute; width: 100px; height: 100px; left: {1}px; top:{0}px;"><span class="tooltiptext">{2}</span></div>'.format(i*100,j*100,temp[i][j]))
with open("datos.html", "a") as file:
    file.write('</body></html>') 