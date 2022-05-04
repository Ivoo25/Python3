'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

P1,P2,P3 = float(input("Ingresa el valor de P1: ")),float(input("Ingresa el valor de P2: ")),float(input("Ingresa el valor de P3: "))
PP = ( P1 + P2 +P3 ) / 3
EP, EF = float(input("Ingresa el valor de EP: ")),float(input("Ingresa el valor de EF: "))
PROM = ( PP + 2*EP + 3*EF ) / 6

print