class OperacionMatematica:
    

    def sumarNumeros(self):
        print(self.val1,self.operacion,self.val2," = ",self.val1+self.val2)

    def restarNumeros(self):
        print(self.val1,self.operacion,self.val2," = ",self.val1-self.val2)

    def multiplicarNumeros(self):
        print(self.val1,self.operacion,self.val2," = ",self.val1*self.val2)

    def dividirNumeros(self):
        print(self.val1,self.operacion,self.val2," = ",self.val1/self.val2)
    
    def aplicarOperacion(operacion):
        sumarNumeros()
        


class calculo:

    suma=OperacionMatematica(10,5,"+")
    suma.sumarNumeros()