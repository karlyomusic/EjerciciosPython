try:
    edad = int(input("Ingrese su edad: "))
    estrato = int(input("Ingrese su estrato: "))
except:
    print("Error: Ingrese un número")

    
if(edad > 18 and edad < 25) and (estrato==1 or estrato==2 or estrato==3):
    print("Aplica para el subsidio")
else:
    print("No aplica para el subsidio")