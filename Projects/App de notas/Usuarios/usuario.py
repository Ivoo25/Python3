import mysql.connector
import datetime as dt

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python",
    port = 3306
)

cursor = database.cursor(buffered=True)


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        fecha = dt.datetime.now()
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)" # null es para que el id se autoincremente, %s es para que se inserte el valor de la variable    
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)
       
        cursor.execute(sql, usuario) 
        database.commit()
        
        return [cursor.rowcount, self]
    
        