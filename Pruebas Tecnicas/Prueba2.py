'''Haz una funcion multiplicar que no utilice el simbolo de multiplicacion * '''

def multiplicar(numero1, numero2):
    num1 = 0
    i = 0
    while i < numero2:
        num1 += numero1
        i+= 1
    return num1


print(multiplicar(8, 8))


        