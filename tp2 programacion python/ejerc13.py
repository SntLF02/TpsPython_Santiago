# Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
# encuentra dentro de la primera.

cadena1=str(input("Ingrese una cadena de caracateres: "))
cadena2=str(input("Ingrese otra cadena de caracteres: "))

# .count() Cuenta cuántas veces aparece una subcadena en la cadena.
cont=cadena1.count(cadena2)

if cont != 0:
    print ("La cadena 2 esta dentro de la cadena 1")
else:
    print ("La cadena 2 no esta dentro de la cadena 1")