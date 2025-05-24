# descenso del gradiente aplicada a una funcion de 2 variables independientes
# funcion:
#           f(x) = (x0 - 2)^2 + (x1 - 2)^2

import numpy as np
import matplotlib.pyplot as plt
#import time 

np.random.seed(11)

def f(x):
    y = (x[0]-2)**2 + (x[1]-2)**2
    return y

plt.ion()
#grafica de superficie
fig = plt.figure() # an empty figure with no Axes
ax = plt.axes(projection='3d')

#grafica de contourf
# Crear la figura y los ejes
# fig, ax = plt.subplots()

x0 = np.linspace(-15,15,40) #vector
x1 = np.linspace(-15,15,40) #vector
X0,X1 = np.meshgrid(x0,x1)  # La función numpy.meshgrid devuelve una lista de matrices de coordenadas a partir de vectores de coordenadas.
x = np.stack((X0,X1))       # hace un stack con los vectores 1-D y el resultante es un array de 2-D

#grafica de superficie
ax.set_xlim3d(-15,15)
ax.set_ylim3d(-15,15)
ax.set_xlabel('x0')
ax.set_ylabel('x1')
ax.plot_surface(X0,X1,f(x),rstride=1,cstride=1, cmap="plasma", alpha= 0.5)
#ax.plot_wireframe(X0,X1,f(x),rstride=1,cstride=1, cmap="cividis")

# #grafica de contourf
# contour = ax.contourf(X0, X1, f(x), cmap="plasma", levels=20)
# fig.colorbar(contour, ax=ax)    #añade una barra de color al costado de la grafica que indica la profundidad

x = [-13,12] #x inicial
h = 0.3     # alpha learn ratio

def gx0(x):
    y = 2*(x[0]-2)
    return y

def gx1(x):
    y = 2*(x[1]-2)
    return y

ant = 0
act = 0
tol = 0.001
i=0

while True:
    i=i+1
    #print(x)
    x = x-h*np.array([gx0(x),gx1(x)])
    ax.scatter(x[0],x[1],f(x),marker='o',facecolor = 'black') #grafica de superficie
    # ax.scatter(x[0], x[1], color='black') #grafica de contourf
    fig.canvas.draw()
    fig.canvas.flush_events()
    #time.sleep(0.01)
    
    act = x[0]

    if abs(act - ant) <= tol:
        #imprime resultados
        print(x)
        print("Nro de pasos: ", i)
        ax.scatter(x[0],x[1],f(x),facecolor='green')
        # ax.scatter(x[0], x[1], color='green')
        plt.show(block=True)
        break
    
    ant = act


