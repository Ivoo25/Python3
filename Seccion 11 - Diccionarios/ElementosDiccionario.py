diccionario = {'Nombre' : "Walter" , 'Apellido' : "Coto" , "Estatura" : 1.80}

print(diccionario)
print(diccionario.keys()) # Imprime las claves del diccionario
print(diccionario.values()) # Imprime los valores del diccionario

print(diccionario["Estatura"]) # Imprime el valor de la clave Estatura

diccionario["Peso"] = "58 kg" # Agrega una nueva clave y valor al diccionario
print(diccionario)

diccionario["Nombre"] = "walter" # Cambia el valor de la clave Nombre
print(diccionario)