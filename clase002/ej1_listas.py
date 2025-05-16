voltajes = [3.2, 3.5, 3.1, 3.6, 3.3, 3.7, 3.0, 3.4, 3.2, 3.5]

# 1. Calcular el promedio
promedio = sum(voltajes) / len(voltajes)
print(f"Promedio del voltaje: {promedio:.2f} V")

# 2. Valor máximo y mínimo
valor_max = max(voltajes)
valor_min = min(voltajes)
print(f"Valor máximo: {valor_max} V")
print(f"Valor mínimo: {valor_min} V")

# 3. Índices donde el voltaje es mayor al promedio
print("Voltajes mayores al promedio en las posiciones:")
for v in voltajes:
    if v > promedio:
        print(f"Mayor al promedio: {v} V")
