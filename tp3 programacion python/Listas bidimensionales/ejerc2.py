# Escribe un programa que calcule la suma de todos los elementos en una lista bidimensional. 

lista=[[1,2,3],[4,5,6],[7,8,9]]
suma=0
for fila in lista:
    print(fila)
    suma=suma+sum(fila)


print("La suma de los elementos de la lista bidimensional da:",suma)
        