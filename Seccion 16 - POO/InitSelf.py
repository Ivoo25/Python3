# class FabricaTelefonos():
#     marca = "Samsung"

#     def ElaborarHuawei(self):
#         self.marca = "Huawei"

# telefono = FabricaTelefonos()
# telefono.ElaborarHuawei()
# print(telefono.marca)

class FabricaTelefonos():
    def __init__(self , marca , color): # Constructor, se ejecuta cuando se crea un objeto, se puede pasar parametros
        self.marca = marca # self es una referencia a la clase, se puede usar para acceder a los atributos de la clase 
        self.color = color

telefono = FabricaTelefonos("Huawei" , "Azul")
print(telefono.marca)
print(telefono.color)