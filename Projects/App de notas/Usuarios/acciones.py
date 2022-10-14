from Misc import mail_validator as r
import Usuarios.usuario as modelo

class Acciones:
    def registro(self):
        print("Vamos a registrarte en el sistema")
        nombre = input("\tIntroduce tu nombre: ")
        apellidos = input("\tIntroduce tus apellidos: ")
        email = input("\tIntroduce tu email: ")        
        while not r.regex_mail_validator().check(email):
            email = input("\tEmail invalido. Introduce tu email: ")
            r.regex_mail_validator().check(email)
        password = input("\tIntroduce tu contraseña: ")
        print("Te has registrado correctamente")
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("Fallo al registrar!")    
    
    def login(self):
        print("Vamos a identificarte en el sistema")
        email = input("\tIntroduce tu email: ")
        password = input("\tIntroduce tu contraseña: ")
        print("Te has identificado correctamente")    