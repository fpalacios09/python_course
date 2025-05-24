# algoritmo del descenso del gradiente

#aplicada a la funcion y = x^2 + 1
# su derivada es 2x

import numpy as np
import matplotlib.pyplot as plt

# se crea la funcion y se grafica
def function(x_):
    y = x_**2 + 1
    return y

x_values = np.linspace(-10,10,500)     # crea un array con valores linealmente espaciados

x_init = 13      #valor inicial (puede ser aleatorio)
alpha = 0.1     #learning rate
precision = 0.0000001

y_list = []
x_list = []
act = 0
ant = 0
i = 0

x = x_init  #comienza el algoritmo con la x inicial

while True:
    i = i+1
    #calcula la derivada en ese punto
    grad = 2*x

    #Actualiza el valor de x usando gradiente descendente
    x = x - alpha*grad

    #almacena los valores en listas
    y_list.append(x**2+1)
    x_list.append(x)

    act = x

    if abs(act - ant) <= precision:
        #imprime resultados
        print("x = ", str(x), "y = ", str(x**2+1))
        print("Nro de pasos: ", i)
        break
    
    ant = act

plt.subplot(1,2,2)
plt.scatter(x_list,y_list,c="r")
plt.plot(x_list,y_list, c="r")
plt.plot(x_values, function(x_values), c="k")
plt.title("Descenso del Gradiente")
plt.show()

