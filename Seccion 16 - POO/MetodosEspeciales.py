class FabricaTelefonos():
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))
    
    def __str__(self): # Se ejecuta cuando se imprime un objeto
        return "El objeto es {}".format(self.marca)
    
    def __del__(self): # Se ejecuta cuando se elimina un objeto
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("Nokia" , "Negro")
print(telefono.marca)
print(telefono)