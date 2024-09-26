# Escribe un programa que permita al usuario ingresar una lista de números y elimine los 
# elementos duplicados.

lista=[]

print("Ingrese 10 numeros:")
for i in  range(0,10):
    lista.append(int(input()))

listaf=list(set(lista))
print("Lista sin duplicados:",listaf)
