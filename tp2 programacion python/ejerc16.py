# Codifique un método que reciba como parámetro una cadena y determine si  la misma  contiene o no números.

frase=input("Ingrese una cadena de caracteres o digitos: ")


class CADENA:
    def contenido(self,frase):
        x=False
        frase=list(frase)

        #Se convierte a lista y se verifica uno por uno los caracteres y se comparan si son digitos numericos o no.
        for i in range(0,len(frase)):
            if frase[i].isdigit()==True:
                x=True

        if x==True:
            print("La cadena de caracteres ingresada contiene numeros")
        else:
            print("La cadena de caracteres ingresada no contiene numeros")
                

cadena=CADENA()
cadena.contenido(frase)

