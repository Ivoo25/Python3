# Capturar excepciones y manejar errores en codigo susceptible a fallos/errores


try:
    nombre = input("Cual es tu nombre?: ")

    if (len(nombre) > 1):
        if(nombre.isalpha()):
            nombre_usuario = "El nombre es " + nombre
              
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteracion")        
    
    
    
#Multiples excepciones

try:
    numero = int(input("Introduce un numero: "))

    print("El cuadrado del numero es: " + str(numero*numero))
except Exception as e:
    print("Ha ocurrido un error:", type(e).__name__) #type(e).__name__ es para mostrar el tipo de error           
'''except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo")
except ValueError:
    print("Introduce un numero correcto")'''
    
    
#Excepciones personalizadas
nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))

try:
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real") #raise es para lanzar una excepcion personalizada y ValueError es el tipo de excepcion
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al master en python {nombre}")    
except ValueError:
    print("Introduce los datos correctamente")    
     