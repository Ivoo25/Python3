#Modulo open dentro del paquete io
from io import open
from operator import indexOf
import pathlib
import shutil #Modulo para copiar, mover y renombrar archivos
import os

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "archivo.txt"
print(ruta)
archivo = open(ruta, "a+") #Permisos: r, w, a, r+, w+, a+, r: lectura, w: escritura, a: añadir, +: lectura y escritura

#Escribir en el archivo
archivo.write("**********Soy un texto metido desde el exterior**********\n")

#Cerrar archivo
archivo.close()


#Abrir Archivo con permisos de lectura
ruta = str(pathlib.Path().absolute()) + "archivo.txt"
archivo_lectura = open(ruta, "r")

#Leer contenido
#contenido = archivo_lectura.read()
'''for elemento in contenido:
    print(elemento)''' #Imprime caracter a caracter. No es recomendable
    
#print(contenido)    

#Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)

for item in lista:
    print(item)
    
for index, item in enumerate(lista): #Enumerate devuelve el indice y el elemento
    print("[{}] {}".format(index, item))    
    
    
#Copiar Archivo
shutil.copyfile(ruta, str(pathlib.Path().absolute()) + "archivo_copiado.txt") #Copiar archivo    

#Mover Archivo
shutil.move(str(pathlib.Path().absolute()) + "archivo_copiado.txt", str(pathlib.Path().absolute()) + "/Shutil/archivo_moved.txt") #Mover archivo

#Eliminar Archivo
os.remove(str(pathlib.Path().absolute()) + "/Shutil/archivo_moved.txt") #Eliminar archivo

print(os.path.abspath("./")) #Devuelve la ruta absoluta del archivo

if(os.path.isfile("./ficheros.py")):
    print("El archivo existe")