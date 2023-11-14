

nombre = input("Introduce tu nombre: ")
if nombre == "":
    nombre = "Desconocido"

while True:
    try:
        edad = int(input("Introduce tu edad: "))
        if 0 <= edad <= 125:
            break
        else:
            print("La edad debe estar entre 0 y 125 años.")
    except ValueError:
        print("Por favor, introduce una edad válida.")

años_por_cumplir = 125 - edad
print("Te llamas", nombre, "y tienes", edad, "años, te quedan aún", años_por_cumplir, "años por cumplir")
