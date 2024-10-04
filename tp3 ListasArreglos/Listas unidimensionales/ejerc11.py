# Escribe un programa que permita al usuario ingresar una lista y un número, y cuente 
# cuántas veces aparece ese número en la lista. 
lista=[]


print("Ingrese 7 numeros para una lista:")
for i in  range(0,7):
    lista.append(int(input()))

num=int(input("Ingrese un numero para contarlo:"))
cont=lista.count(num)

print(f"La cantidad de veces que aparece el numero {num} en la lista {lista} es de: {cont}")
