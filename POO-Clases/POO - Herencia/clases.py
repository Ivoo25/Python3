#Herencia: Es la capacidad que tiene una clase de heredar atributos y métodos de otra clase. Y la clase que hereda se llama subclase y la clase de la que hereda se llama superclase.

class Persona:
    """ 
    nombre
    apellido
    altura
    edad
    """
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad            
        
    def hablar(self):
        return "Estoy hablando"    
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):
    """
    Lenguaje
    Experiencia
    """
    def __init__(self): #Constructor
        self.lenguajes = ["HTML", "CSS", "JavaScript", "PHP"]
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes.append(lenguajes)
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu PC"    
    
    
class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() #Llama al constructor de la clase padre
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15
        
    def auditoria(self):
        return "Estoy auditando una red"