try: 
    usuario = input("Ingrese su usuario: ")
except:
    print("Error: Ingrese solo letras")

try:      
    contraseña = int(input("Ingrese su contraseña: "))
except:
    print("Errpr: Ingrese solo números")

    
if usuario == "admin" and contraseña == 1234:
    print("Acceso concedido")
else:
    print("Acceso denegado")