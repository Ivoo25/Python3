'''Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.'''

A = "Rojo"
B = "Verde"
C = "Azul"

candidato = input("¿Qué candidato eliges?: ").upper()

if(candidato == "A"):
    print("Votaste por el partido: ", A)
elif(candidato == "B"):
    print("Votaste por el partido: ", B)
elif(candidato == "C"):
    print("Votaste por el partido: ", C)
else:
    print("Opcion erronea")            