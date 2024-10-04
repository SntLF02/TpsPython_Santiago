numeros = (1, 2, 2, 3, 4, 4, 4, 5) 
# a) Cuenta cuántas veces aparece el número 4 en la tupla. 
# b) Imprime el resultado. 
x=0

for i in numeros:
    if i==4:
        x+=1
print("La cantidad de veces que aparece el numero 4 en la tupla es de:",x)