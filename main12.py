try:
    A = int(input("Ingresa un número: "))
    B = int(input("Ingresa un número: "))
except:
    print("Error: Ingresa")
if A > B:
    print(A,"es mayor a", B)
elif A<B:
    print(A,"es menor a", B)
elif A == B:
    print(A,"es igual a", B)

