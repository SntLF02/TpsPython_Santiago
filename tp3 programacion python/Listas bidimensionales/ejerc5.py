# Escribe un programa que encuentre el valor más grande en una lista bidimensional. 

matriz=[[5,3,8],[2,6,4],[8,1,2]]
maximo=matriz[0][0]

for i in matriz:
    if max(i)>maximo:
        maximo=max(i)
    print(i)

print("El maximo valor en contrado en la matriz es: ",maximo)