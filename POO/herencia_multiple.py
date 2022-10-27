class Padre():
     def hablar(self):
         print("Hablando desde la clase Padre")

class Madre():
    def reir(self):
        print("Reiendo desde la clase Madre")
        
    def hablar(self):
        print("Hablando desde la clase Madre")

class Hijo(Padre, Madre):
     def hablar(self):
         print("Hablando desde la clase Hijo")
 
class Nieto(Hijo):
     pass 
 
 
 
mi_nieto = Nieto()
mi_nieto.hablar() #Prioriza el orden de cual hereda primero. 
mi_nieto.reir() 


print(Nieto.__mro__) #Muestra el orden de herencia de la clase Hijo, Method Resolution Order