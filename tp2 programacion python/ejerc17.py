# Cree una clase FuncionesPrograma y codifique una función estática getFechaString 
# que reciba como parámetro una fecha y retorne la fecha como una cadena literal.  
# Ejemplo recibo 15/10/1900, la salida debe ser Quince de Octubre de mil novecientos. 
# Cree una clase Principal que contenga un método main y haga uso de la función getFechaString. 
import datetime
#No tengo ni idea que hacer
fechamanual=input("Ingrese una fecha ejemplo: 31-08-2024 ")
class FuncionesPrograma:
    @staticmethod
    def getFechaString(fechamanual):
        fechamanual=datetime.strftime("%Y-%m-%d")
        fechaliteral=fechamanual.strftime("%d de $b de %y")
        print(fechaliteral)
days=FuncionesPrograma()
days.getFechaString(fechamanual)
#no terminado, no funciona