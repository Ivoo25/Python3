#Los metodos especiales son aquellos que se utilizan para realizar operaciones con los objetos, para crear funcionalidades que no pueden ser representadas en un metodo regular

from genericpath import exists


mi_lista = [1,2,3,4,5]
print(len(mi_lista)) # 5, len solo esta disponible para listas, no para objetos

class Objeto():
    pass

objeto = Objeto()
#print(len(objeto)) # TypeError: object of type 'Objeto' has no len()
print(objeto) # <__main__.Objeto object at 0x000001F1B1B1F0F0>

class CD():
    def __init__(self, titulo = "Sin titulo", artista = "Sin artista", canciones = 0):
        self.titulo = titulo
        self.artista = artista
        self.canciones = canciones

    def __str__(self): # __str__ es un metodo especial que se utiliza para representar el objeto como una cadena de caracteres
        return "Titulo: " + self.titulo + ", Artista: " + self.artista + ", Canciones: " + str(self.canciones)
    
    def __len__(self):
        return self.canciones # len solo esta disponible para listas, no para objetos, pero con __len__ podemos hacer que len sea disponible para objetos
    
    def __del__(self):
        print("Se ha borrado el objeto")
        
mi_cd = CD("The wall", "Pink Floyd", 10)
print(str(mi_cd)) # Titulo: The wall, Artista: Pink Floyd, Canciones: 10

print(mi_cd.__str__()) # Titulo: The wall, Artista: Pink Floyd, Canciones: 10
 
del mi_cd # elimina el objeto de la memoria
