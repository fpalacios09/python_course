import numpy as np
import matplotlib.pyplot as plt

# Parámetros
V0 = 5
C = 1
t = np.linspace(0, 10, 500)

# Resistencias individuales
R1 = 1
R2 = 2
R3 = 3

# Voltajes para cada R
V1 = V0 * np.exp(-t / (R1 * C))
V2 = V0 * np.exp(-t / (R2 * C))
V3 = V0 * np.exp(-t / (R3 * C))

# Graficar cada uno con estilo distinto
plt.plot(t, V1, 'r-', label='R = 1 Ω')   # rojo, línea sólida
plt.plot(t, V2, 'g--', label='R = 2 Ω')  # verde, línea discontinua
plt.plot(t, V3, 'b-.', label='R = 3 Ω')  # azul, línea punto-guión

# Título, etiquetas y leyenda
plt.title('Descarga de un condensador en un circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje V(t) [V]')
plt.grid(True)
plt.legend()
plt.show()
