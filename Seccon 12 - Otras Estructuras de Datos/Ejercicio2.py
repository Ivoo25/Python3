'''Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa'''
alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
aux = int(input('Ingrese un numero: '))
encontrado = False

for i in range(len(alfabeto)):
    if aux == i:
        print(alfabeto[i])
        encontrado = True
        break
    
if(not(encontrado)):
    print('No se encontro la letra')