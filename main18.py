ancho = float(input("Ingresa el valor del ancho del cuarto: "))
largo = float(input("Ingresa el valor del largo del cuarto: "))

area = ancho * largo

if area <= 12:
    print("El cuarto es pequeño")
elif area >= 20:
    print("El cuarto es grande")
elif area > 12 and area < 20:
    print("El cuarto es mediano")