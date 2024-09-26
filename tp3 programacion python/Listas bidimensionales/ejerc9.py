# Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz 
# identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa 
# principal son 1 y el resto son 0. 

matriz=[[],[],[],[],[]]

print("Matriz identidad inversa:")
for i in range(0,5):

    for j in range(0,5):
        if i==4-j:
            matriz[i].append(1)
        else:
            matriz[i].append(0)
            
    print(matriz[i])
