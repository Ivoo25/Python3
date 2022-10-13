import random as rand

pool_preguntas = ["¿Pasatiempo favorito?", "¿Crees en el amor a primera vista?", "¿Cuál es tu comida favorita?", "¿Estación favorita del año?", "¿Ciudad o campo?", "¿Comida rápida favorita?", "¿Te gustaría tener un superpoder?", "¿Viajarías al futuro o al pasado?", "¿Perros o gatos?", "¿Si tuvieras mucho dinero: lo ahorrarías o lo gastarías?", "¿Tocas algún instrumento?", "¿Te casarías?","¿Bailar o cantar?", "¿Playa o bosque?", "¿Bebida favorita?", "¿Género musical favorito?"] #Preguntas aleatorias de una respuesta

max_rand = len(pool_preguntas) - 1 #Para que no se salga del rango
print("Bienvenido al generador de nombres! Te hare dos preguntas, trata de responderlas usando una sola palabra.\nEmpecemos!")
pregunta_1 = input(pool_preguntas[rand.randint(0, max_rand)] + ": ") #Pregunta aleatoria
pregunta_2 = input(pool_preguntas[rand.randint(0, max_rand)] + ": ") #Pregunta aleatoria

print("El nombre que se me ocurre es...: \n\t\t\t'{}'".format(pregunta_1 + pregunta_2)) #Imprime el nombre