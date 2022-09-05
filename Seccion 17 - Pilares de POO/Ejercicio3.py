'''Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno'''

class Fabrica():
    def __init__(self , llantas , color , precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    @property
    def llantas(self):
        return self._llantas    
    @property
    def color(self):
        return self._color    
    @property
    def precio(self):
        return self._precio
    
    @llantas.setter
    def llantas(self , llantas):
        self._llantas = llantas
        
    @color.setter
    def color(self, color):
        self._color = color
        
    @precio.setter
    def precio(self, precio):
        self._precio = precio            
        
class Moto(Fabrica):
    def __init__(self , llantas , color , precio):
        super().__init__(llantas , color , precio)

class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)               
        
        
Auto = Carro(4 , "Rojo" , 100000)
print(Auto.llantas, Auto.color, Auto.precio)

MotoMami = Moto(2 , "Azul" , 50000) 
print(MotoMami.llantas, MotoMami.color, MotoMami.precio)       