#Escribe un programa que permita al usuario ingresar una lista de números y filtre los números primos.
lista=[]

def nprimos(lista):
    prim=[]

    for num in lista:
        if num % 2 == 0:
            prim.append(num)
    
    return prim


print("Ingrese 5 numeros:")
for i in  range(0,5):
    lista.append(int(input()))

print("Los numeros primos en la lista ingresada son:",nprimos(lista))