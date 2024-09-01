# - Indique si en Python existen o no variables de tipo valor y su contraparte tipo 
# referencia como sucede en otros lenguajes como Java.  

#Los tipos de valor en Python son aquellos cuyas variables almacenan directamente el valor real.
#Esto significa que cuando asignas una variable a otro valor, se crea una nueva copia de ese valor en la memoria. 
#Los tipos de valor más comunes en Python son:
#Enteros, Flotantes. Cadenas, Booleanos
#Los tipos de referencia son aquellos cuyas variables almacenan una referencia o dirección de memoria al objeto real en 
#lugar del valor real en sí mismo. Esto significa que cuando asignas una variable a otra, ambas variables apuntan al mismo
#objeto en la memoria. Los tipos de referencia comunes incluyen:
#Listas, Diccionarios, Conjuntos, Objetos personalizados

#Paso de Argumentos a Funciones
#Cuando pasas variables a funciones, es importante tener en cuenta si son tipos de valor o tipos de referencia.
#Tipos de Valor: No se modifican cuando son pasados como parámetros, porque la función recibe una copia.

def duplicar_numero(num):
    num *= 2
    print("Dentro de la función:", num)

x = 10
duplicar_numero(x)
print("Fuera de la función:", x)  # x sigue siendo 10

#Tipos de Referencia: Sí se modifican cuando son pasados como parámetros, porque la función recibe 
# una copia de la referencia, que apunta a los mismos datos.

def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función:", lista)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función:", mi_lista)  # mi_lista se modifica