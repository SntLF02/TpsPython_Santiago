# Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
# y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
# efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 14.
# Plantee el algoritmo planteando métodos para su resolución. 

suma=0
numero=int(input("Ingrese un numero de tres digitos:"))
while numero<100 or numero>999:
    print("Error")
    numero=int(input("Ingrese otro numero:"))
aux=numero

while aux>0:
    suma += aux % 10
    aux//=10

print(f"La suma de los digitos del numero {numero} es de: {suma}")