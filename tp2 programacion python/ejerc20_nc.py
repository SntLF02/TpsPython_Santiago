# Cree una clase Fracción con dos atributos, numerador y denominador.  
# Agregue a la clase los siguientes 4 métodos e implemente los mismos:  
# sumarFracciones(Fraccion f1, Fraccion f2) 
# restarFracciones(Fraccion f1, Fraccion f2) 
# multiplicarFracciones(Fraccion f1, Fraccion f2) 
# dividirFracciones(Fraccion f1, Fraccion f2) 
# Todos los métodos deben retornar la fracción resultante de la operación. 
# Cree una clase OperacionesFraccion que contenga un método main donde se solicite 
# al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos 
# Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos 
# implementados anteriormente asignando el resultado a una nueva variable de tipo 
# Fracción y mostrando por pantalla el resultado de las operaciones realizadas.  

class Fraccion:
    Fraccionf1=numerador[0]/denominador[0]
    Fraccionf2=numerador[1]/denominador[1]

    def sumarFraccion(Fraccionf1,Fraccionf2):
        return Fraccionf1 + Fraccionf2

    def restarFraccion(Fraccionf1,Fraccionf2):
        return Fraccionf1 - Fraccionf2
    
    def multiplicarFraccion(Fraccionf1,Fraccionf2):
        return Fraccionf1 * Fraccionf2
    
    def dividirFraccion(Fraccionf1,Fraccionf2):
        return Fraccionf1 / Fraccionf2

class operacionesFraccion:
    def main():
        for x in 2:
            num=input("Ingrese un numero como numerador: ")
            num=num.join(" ")
            den=input("Ingrese un numero como denominador: ")
            den=den.join(" ")
        numerador=num.split(" ")
        denominador=den.split(" ")

        print(Fraccion(numerador,denominador).sumarFraccion())
        print(Fraccion(numerador,denominador).restarFraccion())
        print(Fraccion(numerador,denominador).multiplicarFraccion())
        print(Fraccion(numerador,denominador).dividirFraccion())

operacionesFraccion.main()
        
        
