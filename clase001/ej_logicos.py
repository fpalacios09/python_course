edad = int(input("Ingresa tu edad: "))
nacionalidad = input("¿Eres Paraguayo? (si/no): ")

autorizacion = (edad >= 18) & (nacionalidad == "si")

print("¿Puede votar?", autorizacion)
