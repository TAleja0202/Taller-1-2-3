# una tienda da el 15% de descuento por las compras realizadas ejemplo 3

class Tienda():
    compra = 10000
    descuento = (compra * 0.15)
    ttcompra = compra - descuento

pass
negocio = Tienda()
print(f"Muchas gracia por su compra Valor a pagar con descuento es:{negocio.ttcompra}")