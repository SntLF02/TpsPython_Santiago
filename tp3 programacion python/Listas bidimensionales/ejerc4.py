#Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una 
#matriz intercambia sus filas por columnas.

matriz=[[1,2,3],[4,5,6],[7,8,9]]
matrizT=[[],[],[]]

print("Matriz Original:")
for i in matriz:
    print(i)

print("")
print("Matriz Traspuesta:")
for i in range(0,3):
    for j in range(0,3):
        matrizT[i].append(matriz[j][i])
    print(matrizT[i])


