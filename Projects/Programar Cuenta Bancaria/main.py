# Operador de cuenta bancaria
# Clase Persona:
# Atributos: Nombre y Apellido

# Clase Cliente: Hereda de Persona
# Atributos: numero de cuenta y saldo
# Metodos: Imprimir datos del cliente
#              Depositar dinero
#              Retirar dinero

# Programa para hacer tantas operaciones como quiera hasta que decida salir
#   Dos Funciones:
#    1. Crear cliente
#    2. Funcion que organiza la ejecucion de todo el codigo


from tabnanny import check
from os import system

class Persona():
    def __init__(self, nombre, apellido):
        self.__private_nombre = nombre
        self.__private_apellido = apellido

    def get_nombre(self):
        return self.__private_nombre

    def get_apellido(self):
        return self.__private_apellido

    def set_nombre(self, nombre):
        self.__private_nombre = nombre

    def set_apellido(self, apellido):
        self.__private_apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        try:
            self.__private_balance = float(balance)
        except ValueError:
            print("El balance debe ser un numero")

        try:
            self.__private_numero_cuenta = float(numero_cuenta)
        except ValueError:
            print("El balance debe ser un numero")

        super().__init__(nombre, apellido)

    def get_numero_cuenta(self):
        return self.__private_numero_cuenta

    def get_balance(self):
        return self.__private_balance

    def set_numero_cuenta(self, numero_cuenta):
        self.__private_numero_cuenta = numero_cuenta

    def set_balance(self, balance):
        # Si deposito seria +balance, si retiro, -balance
        self.__private_balance += balance

    def __str__(self):
        return ("Nombre: " + self.get_nombre() + ", Apellido: " + self.get_apellido() + ", Numero de cuenta: " + str(self.get_numero_cuenta()) + ", Balance: " + str(self.get_balance()))


def crear_cliente():
    global lista_clientes
    index = 1
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    check_numero = False
    while not check_numero:
        try:
            numero_cuenta = float(
                input("Ingrese el numero de cuenta del cliente: "))
            check_numero = True
        except ValueError:
            print("El numero de cuenta debe ser un numero")

    check_numero = False

    while not check_numero:
        try:
            balance = float(input("Ingrese el balance del cliente: "))
            check_numero = True
        except ValueError:
            print("El balance debe ser un numero")

    check_numero = False

    Cliente_index = Cliente(nombre, apellido, numero_cuenta, balance)
    index += 1
    print("Cliente numero {}, creado con exito!".format(str(index)))
    print(Cliente_index.__str__())

    lista_clientes += [Cliente_index]


def movimientos_cuenta():
    exit = False
    while not exit:
        eleccion = input(
            "Que desea hacer?\n (1) Crear cliente\n (2) Depositar\n (3) Retirar\n (4) Mostrar Clientes\n (5) Salir\n Eleccion: ")
        if eleccion == "1":
            system("cls")
            crear_cliente()         
        elif eleccion == "2":
            system("cls")
            check_numero = False
            while not check_numero:
                try:
                    numero_cliente = int(input("Ingrese el numero del cliente para realizar el deposito: "))                    
                    check_numero = True
                    if numero_cliente > len(lista_clientes):
                        print("El numero de cliente no existe")
                        check_numero = False
                    else:
                        try:
                            cantidad_retiro = float(input("Ingrese la cantidad a depositar para {}: ".format(lista_clientes[numero_cliente-1].get_nombre())))
                            check_numero = True
                            if cantidad_retiro  < 0:
                                print("No podes depositar una cantidad negativa")
                                check_numero = False
                            else:
                                print("Deposito realizado con exito!")
                                lista_clientes[numero_cliente -1].set_balance(abs(cantidad_retiro))
                                print("Su nuevo balance es: {}".format(lista_clientes[numero_cliente -1].get_balance()))    
                        except ValueError:
                            print("La cantidad a depositar debe ser un numero")
                            check_numero = False        
                except ValueError:
                    print("El balance debe ser un numero")
        elif eleccion == "3":
            system("cls")
            check_numero = False
            while not check_numero:
                try:
                    numero_cliente = int(input("Ingrese el numero del cliente para realizar la extraccion: "))                    
                    check_numero = True
                    if numero_cliente > len(lista_clientes):
                        print("El numero de cliente no existe")
                        check_numero = False
                    else:
                        try:
                            cantidad_retiro = float(input("Ingrese la cantidad a retirar para {}: ".format(lista_clientes[numero_cliente-1].get_nombre())))
                            check_numero = True
                            if cantidad_retiro > lista_clientes[numero_cliente -1].get_balance():
                                print("No tiene suficiente dinero en la cuenta")
                                check_numero = False
                            else:
                                print("Retiro realizado con exito!")
                                lista_clientes[numero_cliente -1].set_balance(-cantidad_retiro)
                                print("Su nuevo balance es: {}".format(lista_clientes[numero_cliente -1].get_balance()))    
                        except ValueError:
                            print("La cantidad a retirar debe ser un numero")
                            check_numero = False        
                except ValueError:
                    print("El balance debe ser un numero")
        elif eleccion == "4":
            system("cls")
            if (len(lista_clientes) == 0):
                print("No hay clientes creados")
            else:
                for cliente in lista_clientes:
                    print(cliente.__str__())
        elif eleccion == "5":
            system("cls")
            exit = True
        else:
            print("Opcion invalida")

    print("Saludos!")


print("Bienvenido al programa de operaciones bancarias")
lista_clientes = []
movimientos_cuenta()

