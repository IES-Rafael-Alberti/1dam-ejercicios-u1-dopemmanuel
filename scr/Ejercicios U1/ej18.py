nombre_completo = input("Ingrese su nombre completo: ")

print("Nombre completo en minúsculas:", nombre_completo.lower())
print("Nombre completo en mayúsculas:", nombre_completo.upper())

palabras = nombre_completo.split()
nombre_formateado = " ".join([palabra.capitalize() for palabra in palabras])
print("Nombre formateado: ", nombre_formateado)