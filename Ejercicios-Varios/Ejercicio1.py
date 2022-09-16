'''Hacer un programa que tenga una lista de 8 numeros y haga lo siguiente:
        1. Recorrer la lista y mostrarla en una funcion
        2. Ordenarla y mostrarla
        3. Mostrar su longitud
        4. Buscar algun elemento (que el usuario pida por teclado)'''

#Creo la lista
numeros = [14, 76, 23, 45, 12, 34, 56, 78] # len(numeros) = 8

#Creo la funcion para mostrar la lista
def mostrarLista(lista):
    '''Muestra la lista'''
    for i in lista:
        print(i)        

mostrarLista(numeros)
        
#Ordenar la lista
def ordenarLista(lista):
    '''Ordena la lista'''
    lista.sort()
    return lista

print(ordenarLista(numeros))

print("La longitud de la lista es: {}" .format(len(numeros)))

numeroABuscar = int(input("Introduce el numero que quieres buscar: "))
checknumber = isinstance(numeroABuscar, int)
while not checknumber or numeroABuscar < 0:
    numeroABuscar = int(input("Introduce el numero que quieres buscar: "))
    checknumber = isinstance(numeroABuscar, int)
else:
    print(f"Has introducido el numero {numeroABuscar}")

search = numeros.index(numeroABuscar)
if(search >=0):
    print(f"El numero {numeroABuscar} se encuentra en la posicion {search} de la lista")
else:
    print("El numero no se encuentra en la lista")     
       