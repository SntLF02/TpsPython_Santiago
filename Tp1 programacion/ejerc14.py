import random
cont=1
numrdm=int(random.randint (0,100))
print("La consola escogio un numero del 0 al 100, intente adivinar cual es!")
numero=int(input("Ingrese un numero:"))
while numrdm!=numero:
    if numero>numrdm:
        print("Es muy alto!")
    else:
        print("Es muy bajo!")
    numero=int(input("Ingrese un numero:"))
    cont=cont+1
print("Correcto!! Era el numero",numrdm)
print("Total de intentos:",cont)



