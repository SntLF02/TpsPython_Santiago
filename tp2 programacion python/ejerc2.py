#Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué ocurre? 
# ¿Existe alguna forma de resolverlo? Ejemplifique.  

#ejemplo
a,b,c=3,5,8
lista=[a,b,c]
# si se intenta poner print(lista[3]) esto dara un error como 'ValueError' o 'IndexError'
# ya que el indice que se intenta imprimir por pantalla no existe ya que
# los indices/recorridos empiezan desde 0,1,2.... siendo asi que hay tres elementos en la lista
# y se intento acceder al cuarto.
# para esto verificamos primero si el indice pedido esxite dentro del rango de nuestra lista, y si no
# esta lo indicamos o volvemos a pedir otro indice

indice=int(input("Ingrese el indice al que quiera acceder:"))
while indice>=int(len(lista)):
    print("El indice indicado no existe")
    indice=int(input("Ingrese otro indice:"))

print(f"Lista[{indice}]: {lista[indice]}")


