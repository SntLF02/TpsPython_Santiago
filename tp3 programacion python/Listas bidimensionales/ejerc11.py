# Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido 
# de las agujas del reloj. 

matriz=[[10,11,12,13],[14,15,16,17],[18,19,20,21]]
matrizG=[[],[],[],[]]

print("Matriz Original:")
for i in matriz:
    print(i)

for i in range(0,3):

    for j in range(0,4):
        matrizG[j].append(matriz[2-i][j])

print("Matriz Girada 90°:")
for i in matrizG:
    print(i)
