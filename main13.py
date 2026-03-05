precio = float(input("Ingresa el precio del producto: "))
precio_final = precio*0.10

if precio >= 100.000:
    print("Tiene acceso a descuento")
    print(precio_final)
elif precio <= 100.000:
    print("No tiene acceso a descuento")
    print(precio)

