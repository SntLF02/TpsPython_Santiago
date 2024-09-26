# Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
# debe generar una matriz de ese tamaño, donde los valores son números enteros 
# consecutivos empezando desde 1. 

def matriz(filas,columnas):
    cont=1
    
    for i in  range (0,filas):
        print("[",end=" ")

        for j in range(0,columnas):
            print(cont,end=" ")
            cont+=1

        print("]")

filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))
matriz(filas,columnas)