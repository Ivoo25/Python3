'''
Script que tenga 4 variables:
    1. Lista
    2. String
    3. Entero
    4. Booleano
Imprimir que tipo de dato es cada una de las variables    
'''

v_lista = [1,2,3]
v_string = "Hola Mundo"
v_entero = 123
v_bool = True

def tipo_dato(variable):
    print("La variable {} es de tipo: {}".format(variable,type(variable)))
    

tipo_dato(v_lista)
tipo_dato(v_string)
tipo_dato(v_entero)
tipo_dato(v_bool)    