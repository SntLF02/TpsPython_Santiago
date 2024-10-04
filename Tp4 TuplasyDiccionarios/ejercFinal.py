# Una tienda de tecnología necesita llevar un registro de su inventario. Cada producto 
# tiene asociado un código, una descripción, y un precio. Además, el sistema debe ser capaz de: 
#1. Mostrar todos los productos disponibles. 
#2. Buscar un producto por su código. 
#3. Modificar el precio de un producto. 
#4. Eliminar un producto del inventario. 
#5. Mostrar todos los productos cuyo precio esté en un rango dado por el usuario. 

def mostrar_inventario(inventario):

    for clave,descripcion in inventario.items():
        print(f"Clave del producto: {clave} ; Descripcion: {descripcion[0]}, Precio: ${descripcion[1]}")

def buscar_producto(inventario,cod):

    print("")
    print(f"Producto encontrado: {cod} ; Descripcion: {inventario[cod][0]}, Precio: ${inventario[cod][1]}")


def modificar_precio(inventario,cod,precio):
    inventario[cod]=(list(inventario[cod]))
    inventario[cod][1]=precio
    inventario[cod]=tuple(inventario[cod])

    print("")
    print(f"El precio del Producto con clave: {cod} fue actualizado a ${precio}")

def eliminar_producto(inventario,cod):
    inventario.pop(cod)
    print("")
    print(f"EL producto con clave: {cod} fue eliminado")

def productos_por_rango_de_precio(inventario,rango1,rango2):
    x=False

    print("")
    print(f"Productos en el rango de precio entre ${rango1} y ${rango2}: ")
    print("")

    for clave,descripcion in inventario.items():

        if rango1<=descripcion[1]<=rango2:
             x=True
             print(f"Clave del producto: {clave} ; Descripcion: {descripcion[0]}, Precio: ${descripcion[1]}")

    if x==False:
        print("No se encontro ningun producto")

inventario = { 
"A0001": ("Gabinete", 80), 
"A0002": ("Mother",150), 
"A0003": ("RAM", 40), 
"A0004": ("GPU", 2000), 
"A0005": ("Procesador", 250) 
} 

mostrar_inventario(inventario)
buscar_producto(inventario,"A0003")
modificar_precio(inventario,"A0001",100)
eliminar_producto(inventario,"A0005")

print("")
rango1=int(input("Ingrese un rango de precio para buscar productos, desde: $"))
rango2=int(input("hasta: $"))

productos_por_rango_de_precio(inventario,rango1,rango2) 