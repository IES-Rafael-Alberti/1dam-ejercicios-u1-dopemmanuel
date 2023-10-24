compras = input("Ingrese los productos de la cesta de compra separados por comas: ")
productos = compras.split(",")
for producto in productos:
    print(producto.strip())