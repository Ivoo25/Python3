'''Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.'''

class Calculadora():
    def __init__(self , numero1 , numero2):
        self._numero1 = numero1
        self._numero2 = numero2
     
    @property
    def numero1(self):
        return self._numero1
    
    @property
    def numero2(self):
        return self._numero2
    
    @numero1.setter
    def numero1(self , numero1):
        self._numero1 = numero1
        
    @numero2.setter
    def numero2(self, numero2):
        self._numero2 = numero2
    
    def sumar(self):
        return self._numero1 + self._numero2
    
    def restar(self):
        return self._numero1 - self._numero2
    
    def multiplicación(self):
        return self._numero1 * self._numero2
    
    def división(self):
        return self._numero1 / self._numero2
    
    
prueba = Calculadora(10.5 , 5)

print(prueba.sumar())
print(prueba.restar())
print(prueba.multiplicación())
print(prueba.división())    
                 