import numpy as np
import matplotlib.pyplot as plt

# Generar 100 puntos de temperatura entre 15 y 30 °C
temperatura = np.linspace(15, 30, 100)

# Generar ruido aleatorio pequeño (ruido normal con media 0 y desviación 1)
ruido = np.random.normal(0, 1, 100)

# Calcular presión según la fórmula dada
presion = 100 + 0.5 * temperatura + ruido

# Tamaño de puntos proporcional a la temperatura (escalado para que se vean bien)
sizes = (temperatura - temperatura.min() + 1) * 10  # evita tamaño 0 y escala

# Crear gráfico de dispersión
plt.scatter(temperatura, presion, s=sizes, c=presion, cmap='viridis', alpha=0.7)

# Añadir barra de colores para la presión
cbar = plt.colorbar()
cbar.set_label('Presión (kPa)')

# Etiquetas y título
plt.xlabel('Temperatura (°C)')
plt.ylabel('Presión (kPa)')
plt.title('Gráfico de dispersión: Temperatura vs Presión')
plt.grid(True)

plt.show()
