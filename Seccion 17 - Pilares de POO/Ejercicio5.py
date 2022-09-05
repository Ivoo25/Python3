'''Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.'''

class Universidad():
    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

class Carrera():
    def __init__ (self, especialidad):
        self._especialidad = especialidad
        
    @property
    def especialidad(self):
        return self._especialidad
    
    @especialidad.setter
    def especialidad(self, especialidad):
        self._especialidad = especialidad                
        
class Estudiante(Universidad, Carrera):
    def __init__(self, nombreAlumno, edad, nombre, especialidad):
        Universidad.__init__(self,nombre) #Cuando tenemos herencia multiple, la mejor forma de llamar a los metodos __init__ es esta?
        Carrera.__init__(self, especialidad)
        self._nombreAlumno = nombreAlumno
        self._edad = edad
    
    @property
    def nombreAlumno(self):
        return self._nombreAlumno
    
    @property
    def edad(self):
        return self._edad
    
    @nombreAlumno.setter
    def nombreAlumno(self, nombreAlumno):
        self._nombreAlumno = nombreAlumno
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def imprimirDatos(self):
        print("Nombre: {}, edad: {}, universidad: {}, especialidad: {}".format(self._nombreAlumno, self._edad, self.nombre, self.especialidad))


Ivo = Estudiante("Ivo", 20, "Universidad de los Andes", "Ingenieria de Sistemas")
(Ivo.imprimirDatos())                            