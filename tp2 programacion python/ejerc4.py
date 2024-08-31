# Desarrolle un programa que ayude a una cajera a determinar el número de cont y 
# monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 
# 20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de 
# dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete 
# de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05 
# centavos. Plantee el algoritmo planteando métodos para su resolución.

p200,p100,p50,p20,p10,p5,p2,p1=200,100,50,20,10,5,2,1
c50,c25,c10,c5=0.50,0.25,0.10,0.05
cont=0
sumBilletes=float(0)

cantidad=float(input("Ingrese la cantidad a pagar:"))

while True:
    if sumBilletes+p200<cantidad:
        sumBilletes+=p200
        cont+=1
    else:
        break    
if cont!=0:
    print(f"Se necesitan {cont} billetes de 200 pesos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+p100<cantidad:
        sumBilletes+=p100
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} billete de 100 pesos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+p50<cantidad:
        sumBilletes+=p50
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} billete de 50 pesos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+p20<cantidad:
        sumBilletes+=p20
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesitan {cont} billetes de 20 pesos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+p10<cantidad:
        sumBilletes+=p10
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} billete de 10 pesos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+p5<cantidad:
        sumBilletes+=p5
        cont+=1
    else:
        break
if cont!=0:    
    print(f"Se necesita {cont} billete de 5 pesos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+p2<cantidad:
        sumBilletes+=p2
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesitan {cont} billetes de 2 pesos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+p1<cantidad:
        sumBilletes+=p1
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} billete de 1 peso")  
    cont=0
    print(sumBilletes)
#
while True:
    if sumBilletes+c50<cantidad:
        sumBilletes+=c50
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} moneda de 50 centavos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+c25<cantidad:
        sumBilletes+=c25
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} monedas de 25 centavos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes+c10<cantidad:
        sumBilletes+=c10
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} moneda de 10 centavos")  
    cont=0
    print(sumBilletes)

while True:
    if sumBilletes<cantidad:
        sumBilletes+=c5
        cont+=1
    else:
        break
if cont!=0:
    print(f"Se necesita {cont} moneda de 5 centavos")  
    cont=0
    print(sumBilletes)