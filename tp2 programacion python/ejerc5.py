#Solicite el ingreso de una cadena y elimine todos los espacios de la misma, muestre la cadena resultante.
frasecorta=str("")
frase=str(input("Ingrese una frase: "))

frase=list(frase)
for i in range (0,len(frase)):
    if frase[i] !=(" "):
        frasecorta+=frase[i]

print(frasecorta)
