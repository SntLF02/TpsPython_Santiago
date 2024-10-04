# Escribe un programa que multiplique cada elemento de una lista bidimensional por un 
# valor escalar dado por el usuario. 

matriz=[[5,3,8],[2,6,4],[8,1,2]]

for i in matriz:
    print(i)

x=int(input("Ingrese un valor por el cual se multiplicaran los elementos de la matriz: "))

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=(matriz[i][j])*x
    print(matriz[i])
