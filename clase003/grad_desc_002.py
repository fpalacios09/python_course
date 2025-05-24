import numpy as np
import matplotlib.pyplot as plt

# se crea la funcion y se grafica
def function(x_):
    y = x_**2
    return y

x = np.linspace(-10,10,500)     # crea un array con valores linealmente espaciados
plt.plot(x,function(x))
plt.show()

#funcion de la derivada 
def derivada(x_):
    x_deriv = 2*x_
    return x_deriv

#funcion del gradiente
def gradient(x_start, precision, alpha):
    x_list, y_list = [x_start], [function(x_start)]
    #bucle while


