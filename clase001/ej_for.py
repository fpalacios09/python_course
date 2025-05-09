# un ingeniero necesita calcular todos los posibles valores de consumo
# de corriente para una carga de resistencia variable
# Valores de R en Ohm: 100-200-300-400-500-600-700-800-900-1000 
# para una fuente de tension de 220 V
# Formula: I = V/R

print("Corriente para cada valor R:")
for i in range(1, 11):
    resistencia = i*100
    corriente = 220 / resistencia
    print(f"R = {resistencia} ohm -> I = {corriente:} A")