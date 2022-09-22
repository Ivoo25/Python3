import os #Modulo para trabajar con el sistema de archivos

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta") #Chequeo si existe la carpeta, si no existe la creo
else:
    print("La carpeta ya existe")    
    

#Eliminar carpeta
#os.rmdir("./mi_carpeta") #Elimina la carpeta si esta vacia    

#Copiar carpeta
os.system("copy -r ./mi_carpeta ./mi_carpeta_copiada") #Copiar carpeta