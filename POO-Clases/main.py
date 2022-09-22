#POO
#Defininr una clase (molde para crear mas objetos de este tipo con caracteristicas similares)
#Por ejemplo, coche, persona, animal, etc.

#En Este caso: Coche
class Coche:
    #Atributos o propiedades (variables) de esta clase, son las caracteristicas o piezas de este objeto
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
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
    

coche = Coche() #Instanciar una clase, crear un objeto de esa clase
print(coche) #<__main__.Coche object at 0x0000020B1D1F0D30>
print(type(coche)) #<class '__main__.Coche'>
print(coche.marca) #Ferrari

print("Velocidad actual:", coche.getVelocidad()) #Velocidad actual:  300         
coche.acelerar()
coche.acelerar()  

print("Velocidad actual:", coche.getVelocidad()) #Velocidad actual:  302 

coche.setColor("amarillo")
print(coche.getColor()) #amarillo

objs = []
for i in range(10):
    objs.append(Coche())
    print("Coches creados: ", i+1)
    
print(objs)    