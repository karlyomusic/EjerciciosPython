try:
    temperatura = float(input("Ingresa la temperatura °C: "))
except:
    print("Error: Ingresa un número")

if temperatura <= 15:
    print("Hace frío")
elif temperatura >= 28:
    print("Hace calor") 
else:
    print("Está agradable")