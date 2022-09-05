class Animales():
    def __init__(self , nombre): # Constructor
        self.nombre = nombre # Atributo

class Perro(Animales): # Clase Perro hereda de Animales
    def __init__(self , nombre , sonido):
        super().__init__(nombre) #Llamo al constructor de la clase padre, super es una palabra reservada que hace referencia a la clase padre
        self.sonido = sonido

#super() es una funcion que nos permite acceder a los atributos y metodos de la clase padre
# es asi: super().atributo(parametros)

perro = Perro("Firulais" , "Guau!")
print(perro.nombre)
print(perro.sonido)