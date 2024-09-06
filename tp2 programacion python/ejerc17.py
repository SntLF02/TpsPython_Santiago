# Cree una clase FuncionesPrograma y codifique una función estática getFechaString 
# que reciba como parámetro una fecha y retorne la fecha como una cadena literal.  
# Ejemplo recibo 15/10/1900, la salida debe ser Quince de Octubre de mil novecientos. 
# Cree una clase Principal que contenga un método main y haga uso de la función getFechaString. 

val=False
while val==False:
    fecha=str(input("Ingrese una fecha por ejemplo 05/09/2024 : "))
    try:
        aux=fecha
        aux=aux.split("/")

        if len(aux[0])==2 and len(aux[1])==2 and len(aux[2])<=4:
            d=int(aux[0])
            m=int(aux[1])
            y=int(aux[2])
            if d<=31 and d>=1 and m>=1 and m<=12 and y>=1 and y<=9999:
                val=True
            else:
                print("Fecha fuera de rango")
        else:
            print("Formato de fecha incorrecto")
    except ValueError:
        print("formato de fecha incorrecto")



class Funcionesprograma:

    @staticmethod
    def getFechastring(fecha):

        dias = {
            "01":"uno","02":"dos","03":"tres","04":"cuatro","05":"cinco","06":"seis","07":"siete","08":"ocho","09":"nueve",
            "10":"diez","11":"once","12":"doce","13":"trece","14":"catorce","15":"quince","16":"dieciseis","17":"diecisiete","18":"dieciocho","19":"diecinueve",
            "20":"veinte","21":"veintiuno","22":"veintidos","23":"veintitres","24":"veinticuatro","25":"veinticinco","26":"veintiseis","27":"veintisiete","28":"veintiocho","29":"veintinueve",
            "30":"treinta","31":"treinta y uno" 
        }
        mes ={
            "01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Novienbre","12":"Diciembre"
        }
        #
        unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
        
        def numero_a_palabras(n):
            if n < 10:
                return unidades[n]
            elif n < 100:
                if n<30:
                    return dias[str(n)]
                else:
                    return decenas[n // 10] + (" y " + unidades[n % 10] if n % 10 != 0 else "")
            elif n < 1000:
                return centenas[n // 100] + (" " + numero_a_palabras(n % 100) if n % 100 != 0 else "")
            else:
                return numero_a_palabras(n // 1000) + " mil " + (numero_a_palabras(n % 1000) if n % 1000 != 0 else "")
        #
        fecha=fecha.split("/")

        print(dias[fecha[0]],"de",end=" ")
        print (mes[fecha[1]],"del",end=" ")
        print(numero_a_palabras(int(fecha[2])))


class Principal:

    def main(self,fecha):
        Funcionesprograma.getFechastring(fecha)


principal=Principal()
principal.main(fecha)
