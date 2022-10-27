class Animal():
    
    def __init__(self, name, age, color):
        self.edad = age
        self.__private_nombre = name
        self.color = color
    
    def nacer(self):
        print("Este animal ha nacido")
    
    #Getters and Setters
    def get_nombre(self):
        return self.__private_nombre
    
    def set_nombre(self, name):
        self.__private_nombre = name
        
    def get_edad(self):
        return self.edad
    
    def set_edad(self, age):
        self.edad = age
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color  
    
    def hablar(self):
        print("Hablando desde la clase Animal")              

class Pajaro(Animal):
    
    def __init__(self, name, age, color, altura, vuelo):
        super().__init__(name, age, color)
    
    def hablar(self):
        print("Hablando desde la clase Pajaro")
        
    def volar(self, metros):
        print("Vole, {} metros".format(metros))

class Perro(Animal):
    def hablar(self):
        print("Hablando desde la clase Perro")
print(Pajaro.__bases__)
print(Animal.__subclasses__())

Piolin = Pajaro("Ivo", 2, "Amarillo")
Piolin.nacer()


(Piolin.hablar())