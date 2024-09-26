#Escribe un programa que permita al usuario ingresar una lista de números y eliminar 
#un elemento en un índice especificado. 

lista=[]

print("Ingrese 5 numeros:")
for i in  range(0,5):
    lista.append(int(input()))

print(lista)
x=int(input("Ingrese un indice del elemento que desea eliminar: "))

lista.pop(x)

print("La lista final quedaria: ",lista)