# Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
# encuentra dentro de la primera. 
aux=False
cadena1=str(input("Ingrese una cadena de caracteres: "))
cadena2=str(input("Ingrese otra cadena de caracteres: "))

cadena1=cadena1.split()
cadena2=cadena2.split()

#print(cadena1)
#print(cadena2)
#print(len(cadena1))
#print(len(cadena2))

#recorro las subcadenas de la cadena 1
for i in range (0,len(cadena1)):
    x=i

    #si la cantidad de subcadenas faltantes por recorrer es mayor a al total de subcadenas 
    # de la cadena 2 entonces entra en el if (por que la cadena 2,por su longitud aun entra dentro de la cadena 1
    # si la cadena 2 no entra en la cadena 1 entonces es imposible que la cadena 2 este dentro de la cadena 1)
    # valga la redundancia
    if len(cadena1)-i >= len(cadena2):

        #se recorre las subcadenas de la cadena 2
        for j in range (0,len(cadena2)):

            # si la subcadena de la cadena1[x] es igual a la subcadena de la cadena2[j]
            #  entonces se sigue comparando las siguientes subcadenas de ambas cadenas
            # hasta que se llega a la ultima subcadena de la cadena 2 
            if cadena1[x] == cadena2[j]:   
                aux=True
                x+=1

            #si la subcadena[0] de la cadena 2 no es igual a la subcadena de la cadena 1[i]
            #que i seria desde donde se empieza a comparar la cadena 1 con la 2
            # entonces se rompe el ciclo for anterior, y se vuelve al primer ciclo for aumentado i en 1
            #y empezando a comparar la cadena 2 desde la subcadena siguiente de la cadena 1
            else:
               aux=False
               break
            
        if aux==True:
            print("La cadena 2 se encuentra dentro de la cadena 1")   
            break
    else:
        break

if aux==False:
    print("La cadena n°2 no se encuentra dentro de la cadena n°1")