class Coche:
    #Atributos o propiedades (variables) de esta clase, son las caracteristicas o piezas de este objeto
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    soy_publico = "Hola, soy un atributo publico" #Puede ser accedido desde cualquier parte
    __soy_privado = "Hola, soy un atributo privado" #No se puede acceder desde fuera de la clase
    
    #Constructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas    
    
    #Metodos, son acciones que hace el objeto (coche) (funciones)
    def acelerar(self):
        self.velocidad += 1 #self es para referirse a la clase actual, en este caso Coche
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad    
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def getPrivado(self):
        return self.__soy_privado
    
    def setPrivado(self, privado):
        self.__soy_privado = privado
    
    def getInformacion(self):
        info = "------ Informacion del coche ------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        info += "\n Caballaje: " + str(self.caballaje)
        info += "\n Plazas: " + str(self.plazas)
        info += "\n-----------------------------------"
        return info