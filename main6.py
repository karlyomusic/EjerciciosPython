precio_producto = float(input("Ingrese el precio del producto: "))

IVA = precio_producto * 0.19

Total = IVA + precio_producto

print("El precio del IVA es:", IVA)
print("El precio total es:", Total)