diccionario = {1 : 2 , 2 : 3 , 3 : 4, 'Nombre' : "Ivo"}
diccionario2 = {4 : 5 , 6 : 7}

print(diccionario)

diccionario.copy() # Copia una copia del diccionario
print(diccionario)

diccionario.pop(1) # Elimina un elemento del diccionario, en este caso el elemento con la clave 1
print(diccionario)

print(diccionario.get('Nombre')) # Imprime el valor de la clave 1

diccionario.setdefault('Nombre2', 'Walter') # Agrega una clave y valor al diccionario, si la clave ya existe no se agrega nada
print(diccionario)

diccionario.update(diccionario2) # Agrega un diccionario al diccionario
print(diccionario)


diccionario.clear()   # Elimina todos los elementos del diccionario
print(diccionario)