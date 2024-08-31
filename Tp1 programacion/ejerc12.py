dia=int(input("Ingrese que dia de la semana es:(1,2,3,4,5,6,7)"))
while dia<1 or dia>7:
    print("Incorrecto")
    dia=int(input("Ingrese que dia de la semana es:(1,2,3,4,5,6,7)"))

if dia==1:
    print("El dia Lunes es un dia laboral")
elif dia==2:
    print("El dia Martes es un dia laboral")
elif dia==3:
    print("El dia Miercoles es un dia laboral")
elif dia==4:
    print("El dia Jueves es un dia laboral")
elif dia==5:
    print("El dia Viernes es un dia laboral")
elif dia==6:
    print("El dia Sabado no es un dia laboral")
else:
    print("El dia Domingo no es un dia laboral")


