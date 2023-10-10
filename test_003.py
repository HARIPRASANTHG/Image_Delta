import numpy as np
import matplotlib.pyplot as plt

x_min = 1 
x_max = 5
y_min = 1 
y_max = 5
Nx = 5 #number of steps for x axis
Ny = 5 #number of steps for y axis

x = np.linspace(x_min, x_max, Nx)
y = np.linspace(y_min, y_max, Ny)

#Can then create a meshgrid using this to get the x and y axis system
xx, yy = np.meshgrid(x, y)

#imagine I have some funcion that does someting based on the x and y values
def somefunc(x_value, y_value):
    return x_value+ y_value
    return np.dstack((x_value/5., np.zeros_like(x_value), y_value/5.))


res = somefunc(xx, yy)

plt.figure(dpi=100)
plt.imshow(res)

plt.show()
