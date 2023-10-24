importe_final = float(input("Ingrese el importe final del artículo: "))
iva_pagado = importe_final * 0.10
importe_sin_iva = importe_final - iva_pagado
print("IVA Pagado: ", iva_pagado)
print("Importe sin IVA:", importe_sin_iva)