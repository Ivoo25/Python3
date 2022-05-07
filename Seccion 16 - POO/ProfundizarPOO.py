class FabricaTelefonos():
    def __init__(self , marca , *colores , **modelos): #**modelos es un diccionario y *colores es una lista
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel" , "Negro" , "Azul" , "Verde", m1 = 500 , m2 = 1000, m3 = 70)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512 #Es un atributo temporal
print(telefono.memoria)