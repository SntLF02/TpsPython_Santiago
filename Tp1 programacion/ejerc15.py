print("Criterio de dibisibilidad del 2")
print("Para saber si un numero es divisible por dos hay que comprobar que sea par")
print("----------")
print("Criterio de dibisibilidad del 3")
print("Sumamos las cifras del numero y el resultado de la suma es un numero multiplo de 3")
print("entonces el numero si es divisible por 3")
print("----------")
print("Criterio de dibisibilidad del 5")
print("Para saber si un numero es divisible por 5, dicho numero debe acabar en 0 o 5")
print("----------")
print("Criterio de dibisibilidad del 6")
print("si se cumplen los criterios del 2 y del 3, entonces es divisible por 6")
print("-----------")
print("Criterio de dibisibilidad del 9")
print("Un numero es divisible por 9 cuando la suma de sus digitos es 9 o multiplo de 9")
print("-----------")
print("Criterio de dibisibilidad del 10")
print("Para saber si un numero es divisible por 10, este debe acabar en 0")
print("-----------")
crt2=False
crt3=False
crt5=False
crt6=False
crt9=False
crt10=False
numero=int(input("Ingrese un numero entero:"))
print("El numero",numero)

if numero % 2 == 0:
    print("Cumple con el criterio de divisibilidad del 2")
    crt2=True

aux=numero
suma=0
while aux>0:
    cifra= aux % 10
    suma+=cifra
    aux//=10
if suma % 3 == 0:
    print("Cumple con el criterio de divisibilidad del 3")
    crt3=True

if numero % 10 == 0 or numero % 10 == 5:
    print("Cumple con el criterio de divisibilidad del 5")
    crt5=True

if crt2==True and crt3==True:
    print("Cumple con el criterio de divisibilidad del 6")
    crt6=True

aux=numero
suma=0
while aux>0:
    cifra= aux % 10
    suma+=cifra
    aux//=10
if suma % 9 == 0:
    print("Cumple con el criterio de divisibilidad del 9")
    crt9=True
   
if numero % 10 == 0:
    print("Cumple con el criterio de divisibilidad del 10")
    crt10=True

if crt2==False and crt3==False and crt5==False and crt6==False and crt9==False and crt10==False:
    print("No cumple con ningun criterio")
