try:
    nota = int(input("Ingresa una nota de 0 a 100: "))
except:
    print("Error: Ingresa un numero de 0 a 100")

if nota >60:
    print("Aprobó")
elif nota < 60:
    print("reprobó")


