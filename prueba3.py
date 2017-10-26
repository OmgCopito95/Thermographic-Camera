import matplotlib.pyplot as plt

temp = [2,4,8,3,3,2,1,6,5,8,7,6,4,9],[6,1,7,1,4,3,5,6,7,8,9,7,5,4],[12,1,2,6.3,6,3,2,1,2,3,4,5,6,5],[12,1,2,6.3,6,3,2,1,2,3,4,5,6,5]
#   [1.5,1,1,1]
#    [6,1,2,1]
#    [12,1,2,1]
my_dpi=96
plt.imshow(temp, cmap='hot') #Create image with scale colors
plt.colorbar() #Draw color bar
#plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
#plt.figure(figsize=(10, 10))  # Don't create a humongous figure
plt.savefig('static/images/imagen.png',dpi=my_dpi)
#plt.show()  #Show image