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
sublistas=[]

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

        for i in range(0,filas-1):
            for j in range(1,columnas):
                num=int(input())
        break

    elif X==2:
        print(columnas)

        sublista=[]
        for i in range(0,filas-1):
            for j in range(1,columnas):
                num=random.randint(1,999)
                Lista[i].append(num)
        break

    else:
        print("Error, intente de nuevo")

print(Lista)