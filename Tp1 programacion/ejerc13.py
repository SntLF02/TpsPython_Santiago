numero=int(input("Ingrese un numero entero:"))
cont=int(0)
if numero>1:
    for i in range(1,numero+1):
        if numero % i == 0:
            cont=cont+1
    if cont==2:
        print("El numero",numero,"Es primo")
    else:
        print("El numero",numero,"No es primo")    
else:
    print("El numero",numero,"No es primo")