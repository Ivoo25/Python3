'''Escribir una función que reciba un número entero positivo y devuelva su factorial.'''

num = int(input("Introduce un numero: "))
aux = (num-1)

while(aux > 0):
    num*=aux
    if(aux == 1):
        print("Numero:", num)
    aux-=1    