''' En la variable 'text' dispones de una cadena de texto.
    Debes contas las palabras y devolver cuantas veces se repiten cada una de ellas
    Ejemplo --> 'nadie' aparece 2 veces
    
    text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar" '''
    
    
text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."

def toLowerCase(texto):
    lowercase  = texto.lower()
    return lowercase
    
def clearText(texto):
    cleanedText = texto.replace(",","").replace(".","").replace(";","").replace(":","").replace("!","").replace("?","").replace("¡","").replace("¿","")
    separatedText = cleanedText.split(" ")
    return separatedText

def countWords(texto):
    dictionario = {}
    for i in texto:
        if i in dictionario:
            dictionario[i] += 1 # si ya existe, suma 1
        else:
            dictionario[i] = 1 # si no existe, crea el elemento
    return dictionario             
    
lowercase = toLowerCase(text)
cleanedText = clearText(lowercase)   

countedWords = countWords(cleanedText)

for i in countedWords:
    if(countedWords[i] > 1):
        print('La palabra "{}", aparece {} veces'. format(i, countedWords[i]))
    else: 
        print('La palabra "{}", aparece {} vez'. format(i, countedWords[i]))    