num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if num1 >= num2:
    numIni = num1
    numFin = num2
else:
    numIni = num2
    numFin = num1

serie: str = ""
while numIni <= numFin:
    serie = serie + numIni
    if numIni != numFin:
        serie = serie + "-"
    numIni = numIni + 1

print(serie)