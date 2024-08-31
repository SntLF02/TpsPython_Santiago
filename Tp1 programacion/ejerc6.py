precio=input("Ingrese el precio de un producto:")
precio=float(precio)
iva=float((21*precio)/100)
total=precio+iva
print("El presio final a pagar del producto con el iva de un %21 agregado es de: $",total)