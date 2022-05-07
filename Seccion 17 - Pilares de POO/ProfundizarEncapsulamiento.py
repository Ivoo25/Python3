class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()

#print(a._cuenta)
#a._cuenta = 20
#print(a._cuenta)

print(a.cuenta())

#Si le ponemos un solo _ a un atributo, sigue siendo publico, pero es una practica para nosotros que si vemos eso NO CAMBIEMOS el valor del mismo, es una forma de decir que no se tiene que usar y tenemos que usar sus getters y setters