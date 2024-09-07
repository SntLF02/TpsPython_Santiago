# Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un atributo de nombre operación. 
# Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:  
# sumarNumeros() 
# restarNumeros() 
# multiplicarNumeros() 
# dividirNumeros() 
# El quinto método será el siguiente:  
# aplicarOperacion(operacion){  
# …………………..  
# }  
# Cree una clase Calculo que contenga un método main, donde cree una instancia de la 
# clase OperacionMatematica, asigne 2 valores para las variables de la instancia y 
# ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “
# ”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las operaciones.  

class OperacionMatematica:

    def __init__(self,v1,v2):
        
        self.val1=v1
        self.val2=v2

    def sumarNumeros(self):
        print(f"{self.val1} + {self.val2} = ",end=" ")
        return self.val1 + self.val2

    def restarNumeros(self):
        print(f"{self.val1} - {self.val2} = ",end=" ")
        return self.val1 - self.val2

    def multiplicarNumeros(self):
        print(f"{self.val1} * {self.val2} = ",end=" ")
        return self.val1 * self.val2

    def dividirNumeros(self):
        print(f"{self.val1} / {self.val2} = ",end=" ")
        return self.val1 / self.val2
    
    def aplicarOperacion(self,operacion):
        if operacion=="+":
            return self.sumarNumeros()
        elif operacion=="-":
            return self.restarNumeros()
        elif operacion=="*":
            return self.multiplicarNumeros()
        else:
            return self.dividirNumeros()
        
        
class calculo:

        def main():
            v1=10
            v2=5

            opr=["+","-","*","/"]
            for i in opr:
                p=OperacionMatematica(v1,v2)
                print(p.aplicarOperacion(i))

calculo.main()