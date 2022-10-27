class Vaca():
    def __init__(self, nombre):
        self.__private_nombre = nombre
    
    def get_nombre(self):
        return self.__private_nombre
        
    def hablar(self):
        print(self.get_nombre() + " dice muuu")

class Oveja():
    def __init__(self, nombre):
        self.__private_nombre = nombre
    
    def get_nombre(self):
        return self.__private_nombre
        
    def hablar(self):
        print(self.get_nombre() + " dice beee")
        
 

vaca_1 =  Vaca ( "Berta" )
oveja_1 =  Oveja ( "Lola" )

vaca_1.hablar()
oveja_1.hablar()        

animales = [vaca_1, oveja_1]
for animal in animales:
    print("Desde la lista: ")
    animal.hablar() # Polimorfismo, el método hablar() se comporta de forma diferente según el objeto que lo invoque 
    print("\n")           

    
def animal_habla(animal):
    print("Desde la funcion:")
    animal.hablar()
        
animal_habla(vaca_1)
animal_habla(oveja_1)       