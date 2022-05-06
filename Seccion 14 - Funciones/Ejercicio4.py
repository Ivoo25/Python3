'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''

def impuesto(factura, iva):
    agregar = iva
    total = factura
    if(iva is None):
        agregar = 21.0
    total = (total* (agregar/100))  
    return(factura + total)

print(impuesto(1000, 21))
    