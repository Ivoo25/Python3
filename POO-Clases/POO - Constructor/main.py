from coche import Coche

carro = Coche("Amarillo", "Ferrari", "Aventador", 300, 500, 2)
print(carro.marca, carro.modelo, carro.color) #Ferrari Aventador Amarillo

try:
    carro2 = Coche("Amarillo")
except Exception as e:
    print("Ha ocurrido un error:", type(e).__name__)
    
    
print(carro.getInformacion())

#Detectar tipado

if type(carro) == Coche:
    print("Es un objeto tipo Coche")
else:
    print("No es un objeto tipo Coche")
    
print(carro.soy_publico)
print(carro.getPrivado())