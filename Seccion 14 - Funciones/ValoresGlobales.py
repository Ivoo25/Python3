def valores():
    global num1 # Declaramos la variable global, ya que si estuviera sin el global y solo en la funcion, estaria unicamente en este scope
    global num2
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores())
print(valores())
print(valores())

resta = num1 - num2
print(resta)