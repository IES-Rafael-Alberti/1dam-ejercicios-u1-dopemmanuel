
def precio_final(importe_sin_iva, tipo_de_iva):
    return (importe_sin_iva + tipo_de_iva / 100)

importe_sin_iva = float(input("Ingrese el importe sin IVA del artículo: "))
tipo_de_iva = float(input("Ingrese el tipo de IVA aplicado (porcentaje): "))
precio_final = importe_sin_iva * 1 + tipo_de_iva / 100
print("El precio final del artículo con IVA es:", precio_final)
