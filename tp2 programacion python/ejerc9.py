# Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. 
# Muéstralos en línea recta, separados por un espacio entre cada carácter. 

codigo=str("")
cadena=str("La lluvia en Mendoza es escasa")
cadena=list(cadena)

for i in range(0,len(cadena)):
    codigo=codigo + str(ord(cadena[i])) + " "

print(codigo)