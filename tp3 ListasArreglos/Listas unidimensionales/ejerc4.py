# Escribe un programa que pida al usuario una lista de números y cuente cuántos de 
# ellos son pares y cuántos son impares.

lista=[]
impar=[]
par=[]
print("Ingrese 5 numeros:")
for i in  range(0,5):
    lista.append(int(input()))
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])

print("Cantidad de numeros pares ingresados:",len(par))
print("Cantidad de numeros impares ingresados:",len(impar))