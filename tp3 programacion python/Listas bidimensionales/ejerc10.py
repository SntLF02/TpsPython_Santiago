# Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique 
# si una matriz es simétrica. 

matriz=[[1,2,3],[2,5,6],[3,6,9]]
matrizT=[[],[],[]]

print("Matriz Original:")
for i in matriz:
    print(i)

print("Matriz Traspuesta:")
for i in range(0,3):
    for j in range(0,3):
        matrizT[i].append(matriz[j][i])
    print(matrizT[i])

if matriz==matrizT:
    print("Es una matriz simetrica")
else:
    print("No es una matriz simetrica")