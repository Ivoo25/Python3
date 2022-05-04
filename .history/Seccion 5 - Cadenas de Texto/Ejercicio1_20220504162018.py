'''
Ejercicio 1

Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
'''

aux = "Te quiero solo como amigo" 
print(aux[:2]) # Imprime los dos primeros caracteres
print(aux[-3]) # Imprime los tres últimos caracteres
print(aux[0:len(aux):2]) # Imprime la cadena cada dos caracteres
print(aux[::-1]) # Imprime la cadena en sentido inverso
pr