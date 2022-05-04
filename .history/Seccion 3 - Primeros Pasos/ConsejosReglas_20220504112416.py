import keyword
from pyclbr import Function
imprimir = 420

##
# Las variables no pueden empezar con numeros
# Las variables no pueden tener caracteres especiales
# Las variables no pueden tener espacios
# Las variables no pueden tener mas de una palabra
# Las variables no pueden ser palabras reservadas
##
    

print(keyword.kwlist) ## trae las palabras resevadas, no se pueden usar para declarar una variable

#function to get average time of running pc in seconds
Function("time.time").__module__ ## trae el modulo de la funcion