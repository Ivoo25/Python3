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


mi_pajaro = Pajaro()
print(mi_pajaro.get_color())

mi_pajaro.set_color("verde")
print(mi_pajaro.get_color())
print(mi_pajaro.get_alas())
mi_pajaro.volar(20)
mi_pajaro.piar()