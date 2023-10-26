
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

if num1 == num2:
    print("Los números no pueden ser iguales")
else:
    if num1 > num2:
        num1, num2 = num2, num1

    count = num2 - num1 - 1
    print(f"El número menor es el {num1} y entre ellos existen {count} números enteros")
