# Cargar una Lista de números decimales de tamaño MXN y mostrar los datos 
# cargados. El tamaño de la Lista debe ser solicitado e ingresado por el usuario, 
# indicando un valor entero para las filas y un valor entero para las columnas, el 
# valor mínimo valido debe ser de 3x2, crear la Lista y solicitar los valores 
# numéricos para cargar de datos en cada posición. La carga de los datos puede ser 
# manual, donde los datos serán ingresados por el usuario  o aleatoria, donde los 
# números serán generados automáticamente, ambos casos en el rango de 1 a 999. 
# El sistema preguntara al usuario como quiere hacer la carga de valores.
import random
Lista=[]

while True:

    filas=int(input("Ingrese la cantidad de filas no menor a 3: "))
    if filas>=3:
        break
    else:
        print("Error")

while True:

    columnas=int(input("Ingrese la cantidad de columnas no menor a 2: "))
    if columnas>=2:
        break
    else:
        print("Error")

print(Lista)

while True:
    X=int(input("Como desea cargar los numeros de la lista, Manualmente(ingrese '1') o generados aleatoriamente(ingrese '2'): "))

    if X==1:
        print(f"Ingrese {filas*columnas} numeros: ")

        for i in range(0,filas):

            sublista=[]
            print(f"Fila n°:{i+1}")

            for j in range(0,columnas):
                num=int(input())
                sublista.append(num)

            Lista.append(sublista)
        break

    elif X==2:
        print(columnas)


        for i in range(0,filas):

            sublista=[]

            for j in range(0,columnas):
                num=random.randint(1,999)
                sublista.append(num)

            Lista.append(sublista)
        break

    else:
        print("Error, intente de nuevo")

# Mostrar la Lista resultante por pantalla en formato de Lista (filas y columnas)

for i in Lista:
    print(i)
print("")

# Generar una nueva Lista de N filas por 1 columna que contenga en cada celda de 
# la columna la sumatoria de las celdas de cada una de las filas de la Lista cargada 
# en el punto 1.

ListaSum=[]

for i in Lista:
    X=0
    sublista=[]

    for j in i:
        X+=j

    sublista.append(X)
    ListaSum.append(sublista)

#Mostrar la Lista resultante por pantalla. 
for i in ListaSum:
    print(i)
print("")

# Generar una nueva Lista de tamaño N filas por 2 columnas donde la primer 
# columna contenga los valores calculados en el punto 3 pero ordenados de 
# Mayor a Menor, y en la segunda columna asignar el valor de la fila que poseía 
# originalmente en la Lista del punto 3. 

ListaOrd=ListaSum

for f in range(0,len(ListaOrd)):
    ListaOrd[f].append(f+1)

for i in range(0,len(ListaOrd)):
    sublista=[]

    for j in range(i,len(ListaOrd)):

        if ListaOrd[j][0]>ListaOrd[i][0]:
            aux=ListaOrd[j]
            ListaOrd[j]=ListaOrd[i]
            ListaOrd[i]=aux

# Mostrar la Lista resultante por pantalla.
for i in ListaOrd:
    print(i)
print("")

# Finalmente sume los elementos de la columna 1 de la Lista del punto 5 y 
# muestre el resultado de la sumatoria por pantalla.

sum=0

for i in range(0,len(ListaOrd)):

    if i != len(ListaOrd)-1:
        print(ListaOrd[i][0],end=" + ")
    else:
        print(ListaOrd[i][0],end=" = ")
    sum+=ListaOrd[i][0]
print(sum)

