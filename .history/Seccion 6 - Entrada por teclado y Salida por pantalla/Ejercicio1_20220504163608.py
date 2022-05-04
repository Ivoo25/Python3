'''Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”'''

from re import X


a = float(input("Ingresa el valor de 'a': "))
b = float(input("Ingresa el valor de 'b': "))
c = float(input("Ingresa el valor de 'c': "))


X1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)