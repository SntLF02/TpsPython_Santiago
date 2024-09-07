# Desarrolle un programa que ayude a una cajera a determinar el número de cont y 
# monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 
# 20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de 
# dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete 
# de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05 
# centavos. Plantee el algoritmo planteando métodos para su resolución.

monedas=["50 centavos","25 centavos","10 centavos","5 centavos","2 centavos","1 centavo"]
valMonedas=[0.50,0.25,0.10,0.05,0.02,0.01]

billetes=["200 pesos","100 pesos","50 pesos","20 pesos","10 pesos","5 pesos","2 pesos","1 peso"]
valBilletes=[200,100,50,20,10,5,2,1]

cantidad=float(input("Ingrese un precio a pagar:"))
suma=float(0)
cont=int(0)

for i in range(0,8):
    while True:
        if suma+valBilletes[i]<=cantidad:
            suma+=valBilletes[i]
            cont+=1
        else:
            break

    if cont!=0:
        print(f"Se necesitan {cont} billetes de {billetes[i]}")  
        cont=0
        print(f"${suma}")

for j in range(0,6):
    while True:
        if suma+valMonedas[j]<=cantidad:
            suma+=valMonedas[j]
            cont+=1
        else:
            break

    if cont!=0:
        print(f"Se necesitan {cont} monedas de {monedas[j]}")  
        cont=0
        print(f"${suma}")
