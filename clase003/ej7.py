import numpy as np
import matplotlib.pyplot as plt

# Crear dominio
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.linspace(-2*np.pi, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)

# Función z = cos(x)*sin(y)
Z = np.cos(X) * np.sin(Y)

# Crear figura y eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar superficie
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Añadir barra de colores
fig.colorbar(surf, shrink=0.5, aspect=10)

ax.set_title('z = cos(x) * sin(y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
