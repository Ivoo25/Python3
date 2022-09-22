##Creacion de modulo

def holaMundo(nombre):
    return f"Hola {nombre}"

def calculadora(numero1,numero2,basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divi = numero1 / numero2
    cadena = ""
    
    if basicas != False:
        cadena += "Suma: " + str(suma) + " "
        cadena += "Resta: " + str(resta) + " "
    else:
        cadena += "Multiplicacion: " + str(multi) + " "
        cadena += "Division: " + str(divi) + " "
        
    return cadena