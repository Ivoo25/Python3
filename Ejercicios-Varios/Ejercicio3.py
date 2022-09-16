'''
Crear un programa que compruebe si la variable esta vacia, si lo esta que la rellene con un texto en minuscula y lo muestre en mayuscula
'''
import random

texto = ""

if texto:
    print(texto.upper())
else:
     texto = input("Ingrese un texto: ").lower()
     print(texto.upper())
     