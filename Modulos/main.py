'''
Modulos son funcionalidades ya hechas para reutilizar
En python hay muchos modulos que ya vienen en el lenguaje y se pueden consultar aqui: docs.python.org/3/py-modindex.html
'''
##Podemos crear nuestros modulos y llamarlos desde otros archivos
import imp
from mimodulo import *

print(holaMundo("Ivo"))
print(calculadora(3,5))

#Modulo Fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(type(fecha_completa))

print(fecha_completa.strftime("%d/%m/%Y %H:%M:%S"))

#Modulo Matematicas
import math

print("Raiz cuadrada de 10: ",math.sqrt(10))
print("Numero PI [Redondeado]: ",round(float(math.pi),2))
print("Numero PI [Sin Redondear]: ",math.pi)
print("Redondear [Alza]: ",math.ceil(6.5678))
print("Redondear [Baja]: ",math.floor(6.5678))

#Modulo Random
import random

print("Numero aleatorio [0-1]: ",random.random())
print("Numero aleatorio [1-100]: ",random.randint(1,100))