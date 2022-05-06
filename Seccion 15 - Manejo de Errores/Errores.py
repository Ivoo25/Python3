while True: #Hasta que no introduzca un valor correcto no salgo de este bloque
    try:
        edad = int(input("Introduce tu edad: "))
        print("Tu edad es:",edad)
        break;
    except:
        print("Error, introduce una edad correcta")
    finally: #Este bloque se ejecuta siempre, independientemente de si hay error o no
        print("Saliendo del programa")    
        