'''Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''
aux = int(input("Introduce un numero: "))
aux2 = int(input("Introduce otro numero: "))


for i in range(aux, aux2):
    if(i % 2 == 0):
        continue
    else:
        print(i)