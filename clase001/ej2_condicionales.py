# Verificar si un sistema está en sobrecarga
# Un ingeniero debe realizar un codigo para verificar si el sistema esta sobrecargado,
# la potencia maxima que puede permitirse es de 1000 W 
# introducir los valores de voltaje y corriente para calcular la potencia y 
# determinar la potencia del sistema y si esta en sobrecarga o no
# medidor:  mayor a 1000 -> sobrecarga
#           mayor a 500 -> cerca del limite
#           cualquier valor hasta 500 -> sistema funcionando correctamente

voltaje = float(input("Voltaje del sistema (V): "))
corriente = float(input("Corriente del sistema (A): "))

potencia = voltaje * corriente

if potencia > 1000:
    print("¡Sistema en sobrecarga!")
elif potencia > 500:
    print("Cerca del límite")
else:
    print("Sistema funcionando normalmente")
