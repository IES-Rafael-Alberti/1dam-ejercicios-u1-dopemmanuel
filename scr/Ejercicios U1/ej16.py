precio_por_barra = 3.49
barras_no_frescas = int(input("Ingrese el número de barras no frescas vendidas: "))
costo_total = barras_no_frescas * precio_por_barra * 0.4
print("Precio habitual por barra: ", precio_por_barra)

print("Descuento por no ser frescas: ", precio_por_barra * 0.6)

print("Costo total de las barras no frescas: ", costo_total)