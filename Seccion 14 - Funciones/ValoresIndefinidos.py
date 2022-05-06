def argumento(*num): # el * indica que se reciben varios argumentos pero no es seguro cuantos
    return type(num)

print(argumento(10 , 20 , 30 , 40 , 50))