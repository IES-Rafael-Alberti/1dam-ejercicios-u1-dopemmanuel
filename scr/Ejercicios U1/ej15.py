capital = float(input("Ingrese la cantidad de dinero depositada: "))

tasa_interes = 0.04

saldo_1_anio = capital * 1 + tasa_interes

saldo_2_anios = saldo_1_anio * 1 + tasa_interes

saldo_3_anios = saldo_2_anios * 1 + tasa_interes

print("Saldo después de 1 año: ", saldo_1_anio)
print("Saldo después de 2 años: ", saldo_2_anios)
print("Saldo después de 3 años: ", saldo_3_anios)
