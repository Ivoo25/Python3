lista = [1,2,4,5,9,7,8,6,3,25,22,10,15,16,18,98,99,100]

def llenarLista():
    num1 = int(input("Por favor, ingrese un numero: "))
    lista.append(num1)
    num2 = int(input("Por favor, ingrese otro numero: "))
    lista.append(num2)
    print("Nueva lista: {}".format(lista))
    ordenarParImpar()
    
def ordenarParImpar():
    listaPar = []
    listaImpar = [lista]
    for i in range(len(lista)):
        if(lista[i] % 2 == 0):
            listaPar.append(lista[i])
        else:
            listaImpar.append(lista[i])
    print("Lista de pares: {}".format(listaPar))
    print("Lista de impares: {}".format(listaImpar))            


llenarLista()