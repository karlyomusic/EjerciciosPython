kilometros = float(input("Ingrese el número de kilometros recorridos: "))
tiempo = int(input("Ingrese el tiempo en minutos: "))

if tiempo <= 10:
    print("Tiene que pagar $5000")
else:
    precio = kilometros*800
    print("Tiene que pagar", precio)