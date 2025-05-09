#hacer una calculadora ingresando dos numeros
#que haga todas las operaciones con esos dos numeros

a = int(input("valor 1: "))
b = int(input("valor 2: "))

suma = a + b        # 13
resta = a - b       # 7
multiplicacion = a * b  # 30
division = a / b    # 3.333...
modulo = a % b      # 1 (residuo de la división)
exponente = a ** b  # 1000 (10^3)
division_entera = a // b  # 3 (división sin decimales)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Modulo:", modulo)
print("Exponente a^b:", exponente)
print("Division entera:", division_entera)

