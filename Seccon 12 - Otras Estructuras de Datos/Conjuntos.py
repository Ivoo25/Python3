conjunto = set((1 , 2 , 3 , 4 , 5)) #Un conjunto es una colección de elementos que no se pueden repetir
#La sintaxis para crear un conjunto es: con [], {} o set()

conjuntoLlaves = {1,2,3,4,5} #A diferencia de un diccionario, un conjunto no tiene claves, por eso no hay : como separador

conjuntoCorchetes = set[(1,2,3,4,5)] #A diferencia de una lista, se le agrega set al principio

print(type(conjunto))
print(type(conjuntoLlaves))
print(type(conjuntoCorchetes)) #GenericAlias es un conjunto