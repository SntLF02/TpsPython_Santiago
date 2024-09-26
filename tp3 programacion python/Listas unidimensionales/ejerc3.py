#Escribe un programa que permita al usuario ingresar una lista y la invierta.

lista=[]

print("Ingrese 5 numeros:")
for i in  range(0,5):
    lista.append(int(input()))

lista.reverse()
print("La lista ingresada pro invertida es:", lista)