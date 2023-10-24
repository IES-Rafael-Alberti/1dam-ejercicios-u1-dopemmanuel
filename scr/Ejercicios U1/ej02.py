def calcular(horas, coste_horas):
    return horas * coste_horas

horas = int(input("Horas de trabajo: "))
coste = int(input("Coste por Horas: "))
total = horas * coste
print("total:",total)