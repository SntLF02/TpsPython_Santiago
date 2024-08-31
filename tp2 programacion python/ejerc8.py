# Reemplaza todas las vocales a de una cadena ingresada por teclado por una vocal e.

cadena=str(input("Ingrese una frase: "))
cadena=list(cadena)

for i in range (0,len(cadena)):
    if cadena[i] == "A":
        cadena[i]="E"
    if cadena[i] == "a":
        cadena[i]="e"
    
cadena="".join(cadena)
print(cadena)
