# Escribe un programa que pida al usuario una lista de números y encuentre el mayor y 
# el menor de ellos. 
lista=[]

print("Ingrese 5 numeros:")
for i in  range(0,5):
    lista.append(int(input()))

print("El mayor numero ingresado en la lista es:",max(lista))
print("El menor numero ingresado en la lista es:",min(lista))