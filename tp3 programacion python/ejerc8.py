# Escribe un programa que identifique y muestre los elementos que se repiten en una lista.
ok=set()
dupl=set()
lista=[]

print("Ingrese 7 numeros:")
for i in  range(0,7):
    lista.append(int(input()))

    if lista[i] in ok:
        dupl.add(lista[i])
    else:
        ok.add(lista[i])

print("Los elementos que se repiten son:",list(dupl))

