from warnings import catch_warnings


lista = ['Python' , 24 , "Rene" , "alexander" , 12]

lista[3] = "Alexander" #Reemplaza el elemento en la posicion 3 de la lista por "Alexander"
print(lista) 
print(lista[3]) #Imprime el elemento en la posicion 3

lista.pop() #Elimina el ultimo elemento de la lista
print(lista)
lista.pop()
print(lista)

lista.remove('Python') #Elimina el elemento "Python" de la lista
print(lista)
