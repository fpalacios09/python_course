import numpy as np
import matplotlib.pyplot as plt

# Función objetivo
def funcion(x):
    return x**2 + 1

# Configuración inicial
x_valores = np.linspace(-10, 10, 500)
x_actual = 9  # Punto inicial
alpha = 0.1    # Tasa de aprendizaje
precision = 0.00001

# Preparar la gráfica
plt.figure()
plt.plot(x_valores, funcion(x_valores), 'k-', label='y = x² + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Descenso del Gradiente - Visualización')
plt.grid(True)
plt.legend()

# Punto inicial
punto = plt.scatter(x_actual, funcion(x_actual), c='red', s=50, label='Punto actual')
plt.xlim(-15, 15)
plt.ylim(-5, 150)

plt.ion()  # Modo interactivo
plt.show()

# Algoritmo de descenso del gradiente
while True:
    # Calcula la derivada (gradiente)
    gradiente = 2 * x_actual
    
    # Guarda el valor anterior para verificar convergencia
    x_anterior = x_actual
    # Actualiza la posición
    x_actual = x_actual - alpha * gradiente
    
    # Actualiza la posición del punto en la gráfica
    punto.set_offsets([x_actual, funcion(x_actual)])
    
    # Actualiza la gráfica
    plt.pause(0.25)
    
    # Condición de parada
    if abs(x_actual - x_anterior) < precision:
        print(f"Mínimo encontrado en x = {x_actual:.5f}, y = {funcion(x_actual):.5f}")
        break

    

plt.ioff()  # Desactiva el modo interactivo
plt.show()