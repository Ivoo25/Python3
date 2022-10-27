class Pajaro():
    
    __private_alas = True
    
    def __init__(self, color = "sin color", especie = "comun"):
        self.__private_color = color # Atributo privado, solo se puede acceder desde la clase
        self.__private_especie = especie # Atributo privado, solo se puede acceder desde la clase
        
    def get_color(self):
        return self.__private_color
    
    def set_color(self, color):
        self.__private_color = color
        
    def get_especie(self):
        return self.__private_especie
    
    def set_especie(self, especie):
        self.__private_especie = especie    
    
    def get_alas(self):
        return self.__private_alas
    
    def piar(self):
        print("pio pio, mi color es {} y soy un {}".format(self.__private_color, self.__private_especie))
        
    def volar(self, metros):
        print("Vole {} metros".format(metros))
        self.piar()  
        
    #Metodos de instancia, metodos que afectan a la instancia, al self, pueden acceder y modificar los atributos del objeto, pueden acceder a otros metodos de la clase      
    #Metodos de clase, declarados con un decorador @classmethod, afectan a la clase, no a la instancia, no pueden acceder a los atributos de la instancia, solo a los de la clase, pueden acceder a otros metodos de la clase, los metodos estaticos no pueden acceder a los atributos de la instancia ni de la clase, solo a otros metodos de la clase
    
    @classmethod
    def poner_huevos(cls, cantidad = 1):
        if cantidad == 1:
            print("Puse un huevo")
        else:
            print("Puse {} huevos".format(cantidad))    
            
    @staticmethod        
    def mirar_al_cielo():
        print("Mirando al cielo")   

mi_pajaro = Pajaro()
print(mi_pajaro.get_color())

mi_pajaro.set_color("verde")
print(mi_pajaro.get_color())
print(mi_pajaro.get_alas())
mi_pajaro.volar(20)
mi_pajaro.piar()

mi_pajaro.poner_huevos(2)
mi_pajaro.poner_huevos()
mi_pajaro.piar()

Pajaro.poner_huevos(2)