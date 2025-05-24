import numpy as np
import matplotlib.pyplot as plt

# Crear dominio
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Evitar división por cero
r_squared = X**2 + Y**2
Z = np.sin(r_squared) / r_squared
Z[r_squared == 0] = 1  # Limite cuando r^2 -> 0

# Crear figura
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Graficar superficie
surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)

# Graficar contorno proyectado en el plano XY (offset z= -0.5)
contour = ax.contour(X, Y, Z, 20, cmap='plasma', offset=-0.5)

# Ajustar vista para que se vea bien el contorno
ax.set_zlim(-0.5, 1)

ax.set_title('z = sin(x² + y²) / (x² + y²)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()
