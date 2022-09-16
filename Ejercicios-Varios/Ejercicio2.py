'''
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
'''
import random

MAX_SIZE = 120
lista_numerica = []

def llenado_lista_while():
    while(len(lista_numerica)< MAX_SIZE):
        lista_numerica.append(random.randint(-1000,1000))
        
    print(lista_numerica)
    print("Largo de la lista [WHILE]: {}".format(len(lista_numerica)))
    lista_numerica.clear()

    
def llenado_lista_for():
    for i in range(MAX_SIZE):
        lista_numerica.append(random.randint(-1000,1000))
        
    print(lista_numerica)
    print("Largo de la lista [FOR]: {}".format(len(lista_numerica)))
    lista_numerica.clear()
    
llenado_lista_while()    
llenado_lista_for()