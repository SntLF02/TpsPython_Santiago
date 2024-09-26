class OperacionesFraccion:
   
    @staticmethod

    def __init__(self, numerador, denominador):
        self.numerador=numerador
        self.denominador=denominador

    def MostrarFraccion(self):
        print(self.numerador,'/',self.denominador)

    def Suma(f1,f2):
        resultado_numerador= f1.numerador * f2.denominador + f2.numerador * f1.denominador
        resultado_denominador = f1.denominador * f2.denominador
        print('Suma: ',resultado_numerador,'/',resultado_denominador)


    def Resta(f1,f2):
        resultado_numerador= f1.numerador * f2.denominador - f2.numerador * f1.denominador
        resultado_denominador = f1.denominador * f2.denominador
        print('Resta: ',resultado_numerador,'/',resultado_denominador)    
    
    
    def Multiplicacion(f1,f2):
        resultado_numerador = f1.numerador * f2.numerador
        resultado_denominador = f1.denominador * f2.denominador
        print('Multiplicacion: ',resultado_numerador,'/',resultado_denominador)

    
    def Division(f1,f2):
        resultado_numerador = f1.numerador * f2.denominador
        resultado_denominador = f1.denominador * f2.numerador
        print('Division: ',resultado_numerador,'/',resultado_denominador)


numeradorf1=int(input('ingrese numerador de la primera fraccion: '))
denominadorf1=int(input('ingrese denominador de la primera fraccion: '))
numeradorf2=int(input('ingrese numerador de la segunda fraccion: '))
denominadorf2=int(input('ingrese denominador de la segunda fraccion: '))


fraccion1 = OperacionesFraccion(numeradorf1,denominadorf1)
fraccion2 = OperacionesFraccion(numeradorf2,denominadorf2)     
fraccion1.MostrarFraccion()
fraccion2.MostrarFraccion()

OperacionesFraccion.Suma(fraccion1,fraccion2)
OperacionesFraccion.Resta(fraccion1,fraccion2)
OperacionesFraccion.Multiplicacion(fraccion1,fraccion2)
OperacionesFraccion.Division(fraccion1,fraccion2)
        

