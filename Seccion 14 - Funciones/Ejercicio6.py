'''Escribir una función que reciba una muestra de números en una lista y devuelva su medida.'''
from operator import length_hint


def medida(*tupla):
    return len(tupla)


print(medida(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))