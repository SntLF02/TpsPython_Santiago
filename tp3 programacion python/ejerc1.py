# Escribe un programa que permita al usuario ingresar una lista de numeros y calcule la 
# suma de todos los elementos en la lista. 
lista=[]
print("Ingrese 5 numeros:")
for i in  range(0,5):
    lista.append(int(input()))

print("La suma de los elementos dentro de la lista da:",sum(lista))
