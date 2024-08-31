verificacion=str("")
contraseña=str(input("Defina su contraseña:"))
cont=int(1)

print("procesando...")
print("procesando...")
print("procesando...")
verificacion=str(input("Ingrese su contraseña para ingresar al sistema:"))
print("procesando...")
print("procesando...")

while verificacion != contraseña and cont!=3:
    cont=cont+1
    print("Contraseña incorrecta, vuelva a intentar")
    verificacion=str(input("Contraseña:"))
    print("procesando...")
    print("procesando...")

if verificacion==contraseña:
    print("Acceso Correcto, Que tenga un buen dia!")
elif cont==3:
    print("Contraseña incorrecta")
    print("Se intento ingresar la contraseña demasidas veces")
    print("Acceso bloquedo")
    print("Fin de programa")
else:
    print("Ocurrio un error inesperado")