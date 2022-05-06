'''Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras'''

for i in range (1,11):
    print(i)

aux = int(input("Introduce un numero: "))
aux2 = int(input("Introduce otro numero: "))

for i in range(aux,aux2):
    print(i)    