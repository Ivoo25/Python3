'''Comisiones del 13% de las ventas de un vendedor'''
print("Bienvenido al programa de comisiones, por cada venta que hagas, un 13% de la misma es destinada a comisiones")
nombre_vendedor = input("Ingresa tu nombre: ")
print("Hola", nombre_vendedor, "empecemos...")
bool_venta = False
sum_venta = 0
while not bool_venta:
    aux_venta = input("Tenes ventas? (si/no): ")
    if aux_venta.lower() == "no":
        bool_venta = True
    elif aux_venta.lower() == "si":
        try:
            venta = float(input("Ingresa el valor de la venta: "))
            sum_venta += (venta*0.13)
        except ValueError:
            print("El valor ingresado no es un numero.")    
    else:
        print("La respuesta ingresada no es valida.")
print("Tus comisiones son de: ${} pesos.".format(round(sum_venta, 2)))
print("Gracias por usar el programa de comisiones")        
