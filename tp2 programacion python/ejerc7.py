# Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas 
# vocales tiene en total. 

vocales=int(0)
cadena=str(input("Ingrese una frase: "))

print(f"La cantidad de caracteres que tiene la cadena '{cadena}' es de: {len(cadena)}")
cadena=list(cadena.upper())

for i in range (0,len(cadena)):
    if (cadena[i]) in ("A","E","I","O","U"):
        vocales+=1

print("La cantidad de vocales que tiene la cadena es:",vocales)

