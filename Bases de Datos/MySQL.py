import mysql.connector
"""
    host
    usuario
    passwd
    database
"""
    
#conexion
database = mysql.connector.connect(
 
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# La conexion, ha sido correcta?
print(database)

# Crear cursor
cursor = database.cursor()
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
##database.commit()
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""    
#Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)               
               """)    

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")    
database.commit()

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000),
    ('Opel', 'Corsa', 6000),
    ('Opel', 'Astra', 18500),
    ('Opel', 'Vectra', 18500)
]
cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
database.commit()