
start = int(input("Introduce el número de inicio: "))
increment = int(input("Introduce el incremento: "))
total = int(input("Introduce el total de la serie: "))

if increment <= 0 or total <= 0:
    print("El incremento y el total deben ser mayores que cero.")
else:
    serie = str(start)
    for i in range(1, total):
        start += increment
        serie += str(-start)
    print("SERIE =>", serie,)
