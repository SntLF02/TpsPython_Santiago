# Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad 
# es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto son 0. 

print("Matriz identidad:")
matriz=[[],[],[],[],[]]
for i in range(0,5):
    for j in range(0,5):
        if i==j:
            matriz[i].append(1)
        else:
            matriz[i].append(0)
    print(matriz[i])
