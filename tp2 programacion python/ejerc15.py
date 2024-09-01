# Indique que sucede si realizo la siguiente declaración de variable:  
# x = None print(x)  
# Explique y ejemplifique el uso de None 

# Que una variable este inicializada con None significa que aun esta no tiene ningun valor asignado en ese momento
# None es el único valor del tipo NoneType

valor = None
if valor is None:
    print("La variable no tiene un valor asignado")
#
def saludar(nombre=None):
    if nombre is None:
        nombre = "invitado"
    print(f"Hola, {nombre}")

saludar()  # Hola, invitado
saludar("Carlos")  # Hola, Carlos
