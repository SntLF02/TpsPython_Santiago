#Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
#promedio de los elementos. 

lista=[]

print("Ingrese 5 numeros:")
for i in  range(0,5):
    lista.append(int(input()))

print("El promedio de los numeros ingresados en la lista es de:",sum(lista)/len(lista))
