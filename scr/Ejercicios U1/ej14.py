payasos = int(input("Ingrese el número de payasos vendidos: "))
munecas = int(input("Ingrese el número de muñecas vendidas: "))

peso_payasos = payasos * 112
peso_munecas = munecas * 75
peso_total = peso_payasos + peso_munecas

print("El peso total del paquete que será enviado es de", peso_total, "gramos.")