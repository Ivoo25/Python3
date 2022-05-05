'''Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal'''

vocal = input("Ingrese una letra: ")

if(vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u"):
    print("Es vocal")
else:
    print("No es vocal")    

