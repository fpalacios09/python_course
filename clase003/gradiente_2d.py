import numpy as np
import matplotlib.pyplot as plt
import time  # Para controlar la velocidad de actualización

# Función objetivo y su derivada
def function(x_):
    return x_**2 + 1

# Configuración inicial
x_values = np.linspace(-10, 10, 500)
x_init = 13
alpha = 0.1
precision = 0.0000001

# Inicialización de variables
y_list = []
x_list = []
act = 0
ant = 0
i = 0
x = x_init

# Configuración de la gráfica
plt.figure(figsize=(12, 6))
plt.ion()  # Modo interactivo

while True:
    i += 1
    # Calcula la derivada en ese punto
    grad = 2 * x
    
    # Actualiza el valor de x usando gradiente descendente
    x = x - alpha * grad
    
    # Almacena los valores en listas
    y_list.append(function(x))
    x_list.append(x)
    
    act = x
    
    # Limpia la gráfica anterior
    plt.clf()
    
    # Gráfica de la función
    plt.subplot(1, 2, 1)
    plt.plot(x_values, function(x_values), 'k-', label='Función: $y = x^2 + 1$')
    plt.scatter(x_list, y_list, c='r', s=20)
    plt.plot(x_list, y_list, 'r-', alpha=0.5)
    plt.scatter(x, function(x), c='b', s=100, label='Posición actual')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Descenso del Gradiente')
    plt.legend()
    plt.grid(True)
    
    # Gráfica del camino de optimización
    plt.subplot(1, 2, 2)
    plt.plot(x_list, 'b-')
    plt.xlabel('Iteración')
    plt.ylabel('Valor de x')
    plt.title('Convergencia del valor de x')
    plt.grid(True)
    
    # Muestra la gráfica
    plt.tight_layout()
    plt.pause(0.05)  # Pausa breve para permitir la actualización
    
    # Condición de parada
    if abs(act - ant) <= precision:
        print(f"x = {x}, y = {function(x)}")
        print(f"Número de pasos: {i}")
        break
    
    ant = act

plt.ioff()  # Desactiva el modo interactivo
plt.show()