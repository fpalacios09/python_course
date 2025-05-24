# algoritmo del descenso del gradiente

#aplicada a la funcion y = x^2 + 1
# su derivada es 2x

x_init = 5      #valor inicial (puede ser aleatorio)
alpha = 0.4     #learning rate
n = 100         # numero de iteraciones

it = []
y = []

x = x_init

for i in range(n):
    print('_________________________')
    print('i: ', str(i+1))

    #calcula la derivada en ese punto
    grad = 2*x
    #Actualiza el valor de x usando gradiente descendente
    x = x -alpha*grad
    #almacena la iteracion y valor correspondiente de y
    y.append(x**2+1)
    it.append(i+1)

    #imprime resultados
    print("x = ", str(x), "y = ", str(x**2+1))

