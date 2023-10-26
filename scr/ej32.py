num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if (num1 >= num2):
    numIni = num1
    numFin = num2
else:
    numIni = num2
    numFin = num1

while (numIni <= numFin):
    print(numIni, end="")
    if (numIni != numFin):
        print("-", end="")
numIni = numIni + 1