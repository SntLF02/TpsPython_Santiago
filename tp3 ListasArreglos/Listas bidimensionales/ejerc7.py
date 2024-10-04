#Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada. 

matriz=[[1,2,3],[4,5,6],[7,8,9]]
diagonal=[]

for i in range(0,3):
    for j in range(0,3):

        if i==j:
            diagonal.append(matriz[i][j])

    print(matriz[i])

print("La diagonal de la matriz es: ",diagonal)