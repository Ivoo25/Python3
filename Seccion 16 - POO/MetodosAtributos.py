class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self , mensaje): #Toda funcion de una clase posee el parametro self, que es una referencia a la clase
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando Música")

telefono = FabricaTelefonos()
print(telefono.marca)
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.llamar("Hola, ¿Con quién hablo?"))
telefono.escucharMusica()