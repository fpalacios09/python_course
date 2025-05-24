import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Crear el vector de tiempo t ∈ [0, 10] con 200 puntos
t = np.linspace(0, 10, 200)

# Paso 2: Calcular la respuesta al escalón unitario: y(t) = 1 - e^(-t)
y = 1 - np.exp(-t)

# Paso 3: Graficar la respuesta
plt.plot(t, y, label='y(t) = 1 - e^{-t}', color='blue')

# Paso 4: Añadir título y etiquetas
plt.title('Respuesta a un Escalón Unitario - Sistema de 1er Orden')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Paso 5: Mostrar la gráfica
plt.show()
