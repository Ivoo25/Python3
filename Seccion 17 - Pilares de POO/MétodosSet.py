class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
        self._indice = 0
        self._numero = 0
    
    @property
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter # setter
    def cuenta(self , cuenta):
        self._cuenta = cuenta
    
    @property
    def contador(self):
        return self._contador

    @contador.setter # setter
    def contador(self , contador):
        self._contador = contador
        
    @property
    def indice(self):
        return self._indice
    
    @indice.setter # setter
    def indice(self, indice):
        self._indice = indice    
        
    @property
    def numero(self):
        return self._numero
    @numero.setter # setter
    def numero(self, numero):
        self._numero = numero

a = A()
# print(a._cuenta)
print(a.cuenta)
a.cuenta = 20 # setter, al poner @cuenta.setter, se convierte en un setter y nos evitamos el llamarlo como una funcion comun
print(a.cuenta)
print(a.contador)
a.contador = 10
print(a.contador)
# a._cuenta = 10
# print(a._cuenta)
