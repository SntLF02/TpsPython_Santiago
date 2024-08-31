#CASTEO: Codifique un programa que solicite el ingreso de un numero decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable a los siguientes tipos de datos, short, int, long, float investigue las 
#diferentes formas de lograr la conversión. Muestre por pantalla el resultado de las conversiones. 

valorDecimal=float(input("Ingrese un numero decimal:"))
valorFloat=float(valorDecimal)
valorInt=int(valorDecimal)
valorStr=str(valorDecimal)
valorBool=bool(valorDecimal)
#En python no existe el tipo de dato short, en java es basicamente un int pero para valores muy pequeños,
#acá se usa predeterminadamente el int para ese caso, lo mismo ocurre con Long, son equivalentes.

print(f"El valor original {valorDecimal} convertido a float(numero decimal): {valorFloat}")
print(f"El valor original {valorDecimal} convertido a int(numero entero): {valorInt}")
print(f"El valor original {valorDecimal} convertido a str(cadena de caracteres): {valorStr}")
print(f"El valor original {valorDecimal} convertido a bool(Valor logico V/F): {valorBool}")