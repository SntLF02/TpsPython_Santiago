# Suma los dígitos de un número ingresado por el usuario de forma recursiva.  
sum=0
num=int(input("Ingrese un numero: "))

def sumDigitos(num,sum):
    suma=num % 10

    if num>0:
        suma=suma + sumDigitos(num//10,sum)
    else:
        suma = 0

    return suma

print(f"La suma de los digitos del numero {num} es igual a {sumDigitos(num,sum)}")
