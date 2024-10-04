# Dado el siguiente texto: 
texto = "manzana naranja manzana pera pera pera naranja manzana" 
# a) Escribe un programa que cuente cuántas veces aparece cada palabra en el 
# texto utilizando un diccionario. 
# b) Imprime el diccionario resultante.

texto=texto.split(" ")
print(texto)

cont = {} 

for palabra in texto: 
    if palabra in cont: 
        cont[palabra] += 1 
    else: 
        cont[palabra] = 1 
 
print(cont)