# Escribe un programa que multiplique cada elemento de una lista de números por un 
# valor ingresado por el usuario. 

lista=[]

for i in  range(0,5):
    
    print("Ingrese un numero:")
    num=int(input())

    print("¿Por cuando desea multiplicar el numero? ")
    lista.append(num*(int(input())))

print("La lista quedaria asi:",lista)

