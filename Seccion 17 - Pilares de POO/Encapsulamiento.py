#Encapsulamiento: Es una caracteristica que permite ocultar el detalle de una clase, para que no se pueda acceder a el desde fuera de la clase. Por ejemplo, si queremos que una clase solo pueda acceder a una parte de sus atributos, o a una parte de sus metodos, entonces podemos encapsular esos atributos y metodos en una clase anonima.

class A():
    def __init__(self):
        self.contador = 0 # atributo de la clase, es publico
    
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0 # __contador es un atributo privado
    
    def incrementar(self):
        self.__contador += 1
    
    def cuenta(self):
        return self.__contador


print("Objeto 1")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)


print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())

try:
    print(b.__contador)
except: # si no existe __contador, entonces no se puede acceder
    print("No puedes acceder a un atributo privado")    