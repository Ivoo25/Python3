'''Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''

aux = int(input("Introduce un numero: "))

i = 0
while(i <= 10):
    print("{} x {} = {}".format(aux, i, aux * i))
    i+=1