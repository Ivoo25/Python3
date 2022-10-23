"""mi_archivo = open("prueba.txt")
print(mi_archivo)
print(mi_archivo.read())
mi_archivo.close()

mi_archivo = open("prueba1.txt", "w")
mi_archivo.write("Hola mundo\n")
mi_archivo.write("Hola mundo\n")
mi_archivo.writelines(["Hola mundo ", "Hola mundo ", "aqui ", "estamos ", "\n"])
from ast import If
import random_spanish_words as rsw
for palabra in ((rsw.wordList)):
    mi_archivo.write((palabra) + '\n')
mi_archivo.close()

mi_archivo = open("prueba1.txt", "a")
mi_archivo.write("Hola mundo!!\n")
mi_archivo.close()

import pathlib
import os

ruta = os.getcwd() # Devuelve la ruta actual del directorio, cwd = current working directory
print (ruta)

ruta = os.chdir('..') # Cambia el directorio actual al directorio padre
mi_archivo = open("Sistema Archivosarchivo.txt", "r")
print(mi_archivo.read())
mi_archivo.close()

ruta = os.makedirs("./Pruebitas") # Crea un directorio nuevo
#mi_archivo = open("./Pruebitas/archivo.txt", "w")
#mi_archivo.close()

ruta = os.path.basename("./Pruebitas/archivo.txt") # Devuelve el nombre del archivo
print(ruta)

ruta = os.path.dirname("./Pruebitas/archivo.txt") # Devuelve el nombre del directorio
print(ruta)

ruta = os.path.split("./Pruebitas/archivo.txt") # Devuelve una tupla con el directorio y el archivo
print(ruta)

#ruta = os.rmdir("./Pruebitas") # Elimina el directorio


from pathlib import Path
carpeta = Path("../Pruebitas")
print(carpeta.exists()) # Devuelve True si existe el directorio
print(carpeta.is_dir()) # Devuelve True si es un directorio
print(carpeta.is_file()) # Devuelve True si es un archivo
print(carpeta.name) # Devuelve el nombre del directorio
print(carpeta.parent) # Devuelve el directorio padre
print(carpeta.suffix) # Devuelve la extensión del archivo
print(carpeta.name) # Devuelve el nombre del archivo

base = Path.home() # Devuelve la ruta del directorio home
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada Familia.txt")) # Crea una ruta
#guia2 = guia.with_name("La Pedrera.txt") # Cambia el nombre del archivo
print(base)
print(guia)
print(guia.parent)
Esp = Path(base, "Europa", "España", "Madrid", "El Prado.txt")
Franc = Path(base, "Europa", "Francia", "Paris", "Torre Eiffel.txt")
Europ = Path(base, "Europa", "Guias.txt")
Europ2 = Path(base, "Europa", "Guias2.txt")
print(Esp)
print(Franc)
print(Europ)
print(Europ2)

guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):
    print("1: ", txt) # Devuelve todos los archivos con extensión .txt

for txt in Path(guia).glob("**/*.txt"):
    print("1:" ,txt) # Devuelve todos los archivos con extensión .txt
"""
import os
import pathlib
#nombre = input("Introduce tu nombre: ")
#edad = input("Introduce tu edad: ")
#os.system("cls")
#print("Hola {}! Tienes {} años.".format(nombre, edad))

#Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
def abrir_leer(archivo_texto):
    archivo_texto += ".txt"
    archivo = open(archivo_texto, "r")
    return archivo.read()

#Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
def sobrescribir(archivo):
    sobrescribir_archivo = open(archivo,"w")
    sobrescribir_archivo.write("contenido eliminado")
    
#Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
def registro_error(nombre_archivo):
    archivo = open(nombre_archivo,"a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()    