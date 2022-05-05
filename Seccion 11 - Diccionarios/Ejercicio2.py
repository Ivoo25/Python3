'''Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}'''


jugadores = {

    1 : "Casillas", 
    15 : "Ramos",
    3 : "Pique", 
    5 : "Puyol",
    11 : "Capdevila", 
    14 : "Xabi Alonso",
    16 : "Busquets", 
    8 : "Xavi Hernandez",
    18 : "Pedrito", 
    6 : "Iniesta",
    7 : "Villa"
}

aux = int(input("Ingrese un numero: "))

if aux in jugadores:
    print("El jugador al que hace referencia es:",jugadores[aux])
else:
    print("Ese numero no se encuentra en el diccionario")    