try:
    sueldo = float(input("Ingresa el sueldo mensual: "))
except:
    print("Error: Ingrese un número")

if sueldo <= 1500000:
    print("No paga impuestos")
    print("Su sueldo es", sueldo)

elif sueldo > 1500000 and sueldo < 3000000:
    impuesto = sueldo*0.05
    print("Su sueldo es", sueldo)
    print("Tiene que pagar de impuesto", impuesto)

elif sueldo >= 3000000:
    impuesto2 = sueldo*0.10
    print("Su sueldo es", sueldo)
    print("Tiene que pagar de impuesto", impuesto2)
