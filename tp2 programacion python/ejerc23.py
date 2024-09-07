# Crea un programa donde se pida el ingreso de una cadena y por medio de 
# recursión mostrar la cadena de forma inversa.  

cadena=str(input("Ingrese una frase: "))
cont=0
alrv=""

def alrevez(cadena,cont,alrv):

    if cont==len(cadena):
        alrv= alrv + ""
    else:
        alrv= alrevez(cadena,cont+1,alrv) + cadena[cont] 
    return alrv

print(alrevez(cadena,cont,alrv))