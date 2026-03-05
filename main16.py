try:
    A = float(input("Ingrese la primera nota: "))
    B = float(input("Ingrese la segunda nota: "))
    C = float(input("Ingrese la tercera nota: "))
except:
    print("Error: Ingrese un número")
    
promedio = A + B + C / 3
resultado = promedio
print ("Su promedio es:", resultado)

if promedio > 59:
    print("Aprobó")
elif promedio < 55:
    print("reprobó")
else:
    print("Va a habilitación")