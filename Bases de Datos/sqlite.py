#SQLite 
import sqlite3 as sql

#Conexión a sqlite
conexion = sql.connect("prueba.db") #Si no existe la crea, si existe la abre, si no se especifica la extensión se crea como .db, si se especifica otra extensión se crea con esa extensión

#Crear cursor, para ejecutar sentencias
cursor = conexion.cursor() #El cursor es un objeto que permite ejecutar sentencias SQL

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(255), descripcion TEXT, precio INT(255))") #Si la tabla no existe la crea, si existe no hace nada

#Guardar cambios
conexion.commit() #Guarda los cambios en la base de datos

#Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer Producto', 'Descripción de mi primer producto', 550)") #Si no se especifica el id, se autoincrementa
conexion.commit()

#Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall() #fetchall() devuelve una lista con todos los registros
print(productos)

for producto in productos:
    print(producto)

for producto in productos:
    print("-----------------------------")
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
print("-----------------------------")    

#Sacar el primer registro de mi tabla
cursor.execute("SELECT * FROM productos")
producto = cursor.fetchone() #fetchone() devuelve el primer registro de la tabla
print(producto)

#Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar varios registros
productos = [
    ("Ordenador portátil", "Buen PC", 700),
    ("Telefono Movil", "Buen Telefono", 700),
    ("Placa Base", "Buena placa", 700),
    ("Tablet 15", "Buena tablet", 700),
    ("Ordenador portátil", "Buen PC", 700)
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos) #El ? es un placeholder, se sustituye por los valores de la tupla
conexion.commit()

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall() #fetchall() devuelve una lista con todos los registros

for producto in productos:
    print("-----------------------------")
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
print("-----------------------------")    

cursor.execute("SELECT * FROM productos where descripcion like '%PC%'") #El $ es para que busque la palabra PC al final de la cadena
productos = cursor.fetchall() #fetchall() devuelve una lista con todos los registros

print("Lista: ", productos)

for producto in productos:
    print("-----------------------------")
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
print("-----------------------------")  

#el commit se usa cuando se hace un insert, update o delete a la conexión, si no se hace el commit no se guardan los cambios en la base de datos

#Cerrar conexion
conexion.close() #Siempre cerrar la conexión
