# Codifique un programa que solicite un número entero mayor a cero y que 
# mediante recursión sume todos los números números naturales desde el número 
# ingresado hasta 1.

num=int(input("Ingrese un numero: "))
result=int(0)
def sum(num,result):
    if num==1:
          print(num,"=", end=" ")
    else: 
        print(num,"+", end=" ")
        
    if num==1:
        return 1
    else:
        result= num + sum(num-1,result) 
    return result

print(sum(num,result))     