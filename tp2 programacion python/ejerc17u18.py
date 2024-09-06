# En la clase FuncionesPrograma codifique una método getFechaDate estática que 
# reciba como parámetro 3 valores enteros, día, mes, anio y retorne la fecha de tipo date correspondiente.  
# En la clase Principal creada en el punto anterior haga uso de la función getFechaDate. 
from num2words import num2words
from datetime import datetime
import locale

# Establecer la configuración regional a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

valid=False

while valid==False:
    fechamanual=input("Ingrese una fecha con el sigiente formato 02-09-2024: ")
    #el bloque try se utiliza para manejar excepciones, es decir, errores que pueden ocurrir durante la ejecución de un programa.
    try:
        fechavalida=datetime.strptime(fechamanual, "%d-%m-%Y")
        valid=True
    except ValueError:
        print("Formato de fecha incorrecto. Intente de nuevo.")

class FuncionesPrograma:
    @staticmethod

    def getFechaDate(dia,mes,anio):

        #Transformar los numeros a palabras
        dia=num2words(dia, lang='es')
        mes=mes.strftime("%B")
        año=num2words(anio, lang='es')
        fechaliteral=f"{dia} de {mes} del {año}"

        print(fechaliteral)


class Principal:

    def main(self,fechavalida):

        
        dia=fechavalida.day
        mes=fechavalida
        anio=fechavalida.year
        FuncionesPrograma.getFechaDate(dia,mes,anio)


principal=Principal()
principal.main(fechavalida)

