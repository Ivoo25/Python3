'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

aux = int(input("Introduce tu edad: "))
i = 0
while(i <= aux):
    print("Cumpliste: {}".format(i))
    i+=1