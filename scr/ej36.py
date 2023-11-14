notas1 = int(input("Cuantas notas vas a introducir?: "))


while notas1 < 1 or notas1 > 100:
    print("Error - el número de notas debe ser un número entero entre 1 y 100")
    total = int(input("Cuantas notas vas a inttroducir?:"))

suma = 0

for i in range (notas1):
    nota2 = float(input("Introduce la nota #{}: ".format(i + 1)))
    suma += nota2

media = suma / notas1
print("La media es", media)