#  Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario  
# pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el 
# resultado por pantalla. 

cadena=str(input("Ingrese una frase:"))
opc=int(input("Ingrese que si desea convertir la frase a mayusculas o minusculas (1/2): "))

while opc <1 or opc>2:
    opc=int(input("Icorrecto elija una opcion: (1/2) "))

if opc==1:
    cadena=cadena.upper()
    print("Su frase en Mayusculas seria:")
else:
    cadena=cadena.lower()
    print("Su frase en Minusculas seria:")
print(cadena)

