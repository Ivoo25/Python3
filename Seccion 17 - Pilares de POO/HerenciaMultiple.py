class A():
    def primera(self):
        return "Esta es la clase A"

class B():
    def segunda(self):
        return "Esta es la clase B"

class C(A , B): # Clase C hereda de A y B
    pass

c = C()
print(c.primera())
print(c.segunda())