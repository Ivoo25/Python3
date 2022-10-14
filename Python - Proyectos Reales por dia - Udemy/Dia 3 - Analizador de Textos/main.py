##Indice de strings
mi_texto = "Hola, soy un texto de prueba"
resultado = mi_texto[0] # H, el primer caracter
print(resultado)
resultado = mi_texto[-1] # a, el ultimo caracter
print(resultado)

#Cual es el caracter que tenemos y queremos ver en que indice esta
try:
    resultado = mi_texto.index("a") #Si pongo una palabra, me devuelve el indice del primer caracter de la palabra, si pongo una palabra que aparece mas de una vez, me devuelve la primera vez que aparece
    print((resultado))
except ValueError:
    print("El caracter no esta en el texto")    
    
#Slicing, extraer sub string
resultado = mi_texto[mi_texto.index("texto"): mi_texto.rindex("o") + 1] # rindex es para buscar de derecha a izquierda
print("Resultado: {}".format(resultado))

texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[texto.index("A")::2] 
print(fragmento)
fragmento = texto[::-1] #Invierte el texto
print(fragmento)

#Metodos
texto = "Hola, soy un texto de prueba, creado por mi"
resultado = texto.upper() #Pasa todo a mayusculas
print(resultado)
resultado = texto.lower() #Pasa todo a minusculas
print(resultado)
resultado = texto.capitalize() #Pone la primera letra en mayuscula
print(resultado)
resultado = texto.title() #Pone la primera letra de cada palabra en mayuscula
print(resultado)
resultado = texto.swapcase() #Pone en mayuscula las minusculas y viceversa
print(resultado)
resultado = texto.replace(" ", "") #Reemplaza un caracter por otro
print(resultado)
resultado = texto.split(" ") #Separa el texto en una lista, por el caracter que le indiquemos
print(resultado)
print(len(resultado)) #Cuantos elementos tiene la lista

a = "Hola"
b = "Mundo"
c = "!"
d = " ".join([a, b, c]) #Une los elementos de una lista en un string, separados por el caracter que le indiquemos
print(d)

resultado = texto.find("x") #Devuelve el indice del primer caracter de la palabra que le indiquemos
print(resultado)
resultado = texto.find("z") #Devuelve el indice del primer caracter de la palabra que le indiquemos, si no lo encuentra devuelve -1
print(resultado)