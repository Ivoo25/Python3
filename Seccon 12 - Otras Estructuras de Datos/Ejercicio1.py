'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''

meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
encontrado = False
aux = int(input('Ingrese un numero: '))

for i in range(len(meses)-1):
    if aux == i:
        print(meses[i])
        encontrado = True
        break

if(not(encontrado)):
    print('No se encontro el mes')
