import matplotlib.pyplot as plt
import numpy as np

#Metodo recolectar datos de puerto serie.

filas = 3
columnas = 4

with open("datos.html", "w") as file:
    file.write('<!DOCTYPE html><html><head><link type="text/css" rel="stylesheet" href="custom.css" media="all"></head><body>')

temp = [1.5,1,1,1],[6,1,2,1],[12,1,2,1]
'''[1.5,1,1,1]
   [6,1,2,1]
   [12,1,2,1]'''

plt.imshow(temp, cmap='hot') #Create image with scale colors
plt.colorbar() #Draw color bar
#plt.show()  #Show image 

for i in xrange (0,filas): # i = columnas
    for j in xrange (0,columnas): # j = filas
        print temp[i][j]
        with open("datos.html", "a") as file:
            file.write('<div style=" background-color: red; position: absolute; width: 100px; height: 100px; left: {1}px; top:{0}px;" ></div>'.format(i*100,j*100))
with open("datos.html", "a") as file:
    file.write('</body></html>') 