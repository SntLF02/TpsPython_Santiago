# Escribe un programa que sume dos listas de números elemento por elemento. Las 
# listas deben tener la misma longitud. 
lista1=[]
lista2=[]
lista3=[]

print("Ingrese 5 numeros para la lista n1:")
for i in  range(0,5):
    lista1.append(int(input()))

print("Ingrese 5 numeros para la lista n2:")
for i in  range(0,5):
    lista2.append(int(input()))

for j in range(0,5):
    lista3.append(lista1[j]+lista2[j])

print(f"La suma en los mismo indices de ambas lista n°1:{lista1} y n°2: {lista2} da como resultado la lista n°3: {lista3}")
