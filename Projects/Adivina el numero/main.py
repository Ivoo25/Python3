import random as rand
input("Bienvenido al juego de adivinar el numero, presiona enter para continuar")
nombre = input("¿Cual es tu nombre? ")
intentos = rand.randint(1, 10)
numero_pensado = rand.randint(1,100)
print("Bienvenido {}! Empecemos...\nTendras {} intentos para adivinar el numero que tengo pensado.\nEl mayor de los exitos!".format(nombre, intentos))

i = 0
numero_correcto = False
while True:
    try:
        numero_usuario = int(input("Piensa un numero del 1 al 100... "))
        break;
    except ValueError:
        print("No has ingresado un numero, intenta de nuevo")    

while i <= intentos:
    if numero_usuario < 1 or numero_usuario > 100:
        numero_usuario = input("El numero debe estar entre 1 y 100... ")
        i += 1
    elif numero_usuario == numero_pensado:
        i += 1
        print("Felicidades {}! Adivinaste el numero! Y solo te tomo {} intentos!".format(nombre, i))
        break
    elif numero_usuario < numero_pensado:
        i += 1
        print("El numero que pensaste es menor al que tengo pensado, intenta de nuevo.\nLlevas ya {} intentos".format(i))
        while True:
            try:
                numero_usuario = int(input("Piensa un numero del 1 al 100... "))
                break;
            except ValueError:
                print("No has ingresado un numero, intenta de nuevo")
    elif numero_usuario > numero_pensado:
        i+=1
        print("El numero que pensaste es mayor al que tengo pensado, intenta de nuevo.\nLlevas ya {} intentos".format(i))
        while True:
            try:
                numero_usuario = int(input("Piensa un numero del 1 al 100... "))
                break;
            except ValueError:
                print("No has ingresado un numero, intenta de nuevo")
                    