class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
    
    @property # getter
    def cuenta(self):
        return self._cuenta
    
    @property # getter
    def contador(self):
        return self._contador


a = A()
# print(a._cuenta)
print(a.cuenta) #No lleva parentesis porque es una propiedad, no un metodo, agregando @property nos evitamos el parentesis
print(a.contador)
# a._cuenta = 10
# print(a._cuenta)
