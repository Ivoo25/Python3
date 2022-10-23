"""diccionario = {'clave1':100,
               'clave2':200,
               'clave3':300,
               'clave4':400,
               'clave5':500}

aux = diccionario.popitem()
print(aux)
print(diccionario)

#Remover lo que esta antes de mi texto principal
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(texto.lstrip(",:_#,:"))


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)"""

def saludar_persona(nombre = "Jane Doe"): #Parametro por defecto, si no se le pasa nada, se le asigna el valor por defecto que en este caso es "Jane Doe"
    """
    Esta funcion saluda a una persona
    """
    print("Hola, {}".format(nombre))

#saludar_persona("Ivo")

import random as rand

from pyparsing import WordStart

def chequear_3_cifras(numero):
    return numero in range(100,1000) #Devuelve True o False si el numero esta en el rango de 100 a 1000, mil no lo incluye

#resultado = chequear_3_cifras(rand.randint(0,10000)) #Genera un numero aleatorio entre 100 y 999
#print(resultado)

def chequear_3_cifras_lista (lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False    
var_lista = []
rango = rand.randint(0,100)
for i in range(rango):
    var_lista.append(rand.randint(0,100000)) #Genera una lista de numeros aleatorios entre 0 y 10000
#print(rango)
#print(var_lista)
    
#print(chequear_3_cifras_lista(var_lista))

def chequear3Cifras(lista):
    aux = []
    for n in lista:
        if n in range(100,1000):
            aux.append(n)
        else:
            pass
    return aux                 

#print(chequear3Cifras(var_lista))

precios_cafe = [
    ('Capuchino', 4.5),
    ('Americano', 3.5),
    ('Cortado', 4.0),
    ('Mocha', 5.0),
    ('Latte', 4.0),
    ('Espresso', 2.5),
    ('Cafe con leche', 3.5),
    ('Cafe solo', 2.5)
]

def cafe_mas_caro(cafes):
    max = 0
    cafe = ""
    for i,c in cafes:
        if c > max:
            max = c
            cafe = i
    
    return "El cafe mas caro es " + cafe + " con un precio de " + str(max)        

#print(cafe_mas_caro(precios_cafe))

import random as rand

size_palitos = ['-', '--', '---', '----', '-----']
#print(size_palitos)

def mezclar_palitos(lista):
    rand.shuffle(lista)
    return lista


def probar_suerte():
    while True:
        try:
            num = int(input("Ingrese un numero del 1 al 5: "))
            if(num not in range(1,6)):
                print("El numero ingresado no es correcto")
            else:
                break    
        except ValueError:
            print("No es un numero")
            continue
    return num    
        
def chequear_intento(lista,posicion):
    print(lista)
    if lista[posicion - 1] == '-':
        return "A lavar los platos!"
    else:
        return "Zafaste de lavar los platos!\n En la posicion que elegiste estaba el palito {}, mientras que el mas chico estaba en la posicion {}".format(lista[posicion - 1], (lista.index('-') + 1))
  
#print(chequear_intento(mezclar_palitos(size_palitos),probar_suerte()))            

def suma(*args):
    total = 0
    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            pass
    return total

#print(suma(1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",5))
            
def sumakw(**kwargs):
    total = 0
    print((kwargs))
    for k,v in kwargs.items():
        print("{}:{}".format(k,v))
        try:
            total += int(v)
        except ValueError:
            pass
    return "Total:" + str(total)        
#print(sumakw(x=3, y=5, z=10))              

def suma_total(a,b,*args,**kwargs):
    total = 0
    total += a
    total += b
    print("El primer valor es {} y el segundo es {}".format(a,b))
    for arg in args:
        print("El valor de los argumentos es {}".format(arg))
    for k,v in kwargs.items():
        print("El valor de los argumentos es {}".format(v))    
    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            pass
    for k,v in kwargs.items():
        try:
            total += int(v)
        except ValueError:
            pass
    return total
args = (1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",5)
kwargs = {"x":3, "y":5, "z":10}
#print(suma_total(1,2,*args,**kwargs))

import random_spanish_words as rsw

def random_word():
    palabra = rand.choice(rsw.wordList)
    while True:
        if len(palabra) > 5:
            return palabra
        else:
            palabra = rand.choice(rsw.wordList)
            continue

print(random_word())