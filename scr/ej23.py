correo = input("Ingrese su correo electrónico: ")
nombre_usuario = correo.split('@')[0]
nuevo_correo = nombre_usuario + '@g.educaand.es'
print("Nuevo correo con dominio educaand.es:", nuevo_correo)
