"""La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta. """

print("Bienvenido al juego del string!")
string_almacenar = input("Ingresa un texto, el que desees: ")
print("Excelente! Ahora ingresa tres letras a tu eleccion.")
letra_1 = input("Ingresa la primera letra: ")
letra_2 = input("Ingresa la segunda letra: ")
letra_3 = input("Ingresa la tercera letra: ")

# 1. Primero:
aux1, aux2, aux3 = 0, 0, 0
for i in string_almacenar.lower():
    if i == letra_1.lower():
        aux1 += 1
    elif i == letra_2.lower():
        aux2 += 1
    elif i == letra_3.lower():
        aux3 += 1

print("La letra '{}' aparece {} vez/ veces, la segunda letra, '{}', aparece {} vez/ veces y la letra '{}', aparece {} vez/ veces".format(letra_1, aux1, letra_2, aux2, letra_3, aux3))

#2. Segundo:
aux4 = string_almacenar.split()
print("El texto ingresado tiene {} palabras.".format(len(aux4)))

#3. Tercero:
print("La primera letra del texto es: '{}', mientras que la ultima es '{}'.".format(string_almacenar[0], string_almacenar[-1]))

#4. Cuarto:
print("El texto invertido se leeria asi:{}".format(string_almacenar[::-1]))

#5. Quinto:
if "python" in string_almacenar.lower():
    print("La palabra 'Python' se encuentra en el texto ingresado.")
else:
    print("La palabra 'Python' no se encuentra en el texto ingresado.")    