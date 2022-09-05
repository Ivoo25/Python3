'''Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''

class Estudiante():
    def __init__(self , nombre , nota):
        self._nombre = nombre
        self._nota = nota
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota
  
  
    @nombre.setter
    def nombre(self , nombre):
        self._nombre = nombre
    
    @nota.setter
    def nota(self, nota):
        self._nota = nota
    
  
    def resultado(self):
        if(self._nota >= 5):
            return "Aprobado"
        else: 
            return "Reprobado"
        

Ivo = Estudiante("Ivo" , 8) 

print(Ivo.resultado())       