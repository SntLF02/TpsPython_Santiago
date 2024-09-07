# Crea un programa que lea una cadena de texto carácter por carácter usando recursión. 

cadena=str(input("Ingrese una frase: "))
cont=0

def leerCadena(cadena,cont):

    if cont==len(cadena)-1:
        print(cadena[cont])
    else:
        print(cadena[cont])
        leerCadena(cadena,cont+1)

leerCadena(cadena,cont)


