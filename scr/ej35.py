"""
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

opcion = 0
while opcion < 1 or opcion > 4:
    print("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): ")
#deberia de ver un "int" aqui
if opcion < 1 or opcion > 4:
    print("Error - No es una opción correcta (1-4)")

if opcion == 1:
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif opcion == 2:
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif opcion == 3:
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif opcion == 4:
    if num2 == 0:
        print("La división por cero no es posible")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
"""

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

opcion = 0
while opcion < 1 or opcion > 4:
    print("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): ")
    opcion = int(input())
    if opcion < 1 or opcion > 4:
        print("Error - No es una opción correcta (1-4)")

if opcion == 1:
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif opcion == 2:
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif opcion == 3:
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")

elif opcion == 4:
    if num2 == 0:
        print("La división por cero no es posible")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
