try:
    edad = int(input("Ingresa tu edad: "))
except:
    print("Error: Ingresa un número")


if edad < 18:
    print("Eres menor de edad")
elif edad > 18:
    print("Eres mayor de edad")

