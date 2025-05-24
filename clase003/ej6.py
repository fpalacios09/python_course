import numpy as np
import matplotlib.pyplot as plt

# Semilla para reproducibilidad
np.random.seed(0)

# Generar 300 valores uniformes entre 0 y 10 para x
x = np.random.uniform(0, 10, 300)

# Generar ruido normal para y y z
ruido_y = np.random.normal(0, 0.5, 300)
ruido_z = np.random.normal(0, 0.5, 300)

# Calcular y y z con las fórmulas dadas
y = 2 * x + np.sin(x) + ruido_y
z = 3 * x - np.cos(x) + ruido_z

# Crear gráfico scatter
# Tamaño proporcional al valor absoluto de z (escalado para mejor visualización)
tamaño = np.abs(z) * 10

scatter = plt.scatter(x, y, s=tamaño, c=z, cmap='plasma', alpha=0.7, edgecolors='black')

# Etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de dispersión con tamaño y color según z')

# Barra de colores para interpretar los valores de z
plt.colorbar(scatter, label='Valor de z')

# Mostrar gráfico
plt.show()