'''Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio'''

def areaCuadrado(base, altura):
    area = base * altura
    return area

def areaCirculo(radio):
    area = 3.1416 * (radio ** 2)
    return area


print(areaCuadrado(10, 20))
print(round(areaCirculo(10),2))