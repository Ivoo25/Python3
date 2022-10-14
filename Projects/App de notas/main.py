'''
Proyecto Python y My SQL:
-Abrir asistente
-Login o registro
-Si elegimos registro, creará un usuario en la bbdd
-Si elegimos login, identificará al usuario y nos preguntará
-crear nota, mostrar notas, borrarlas
-crear nota: pedirá título y contenido
-mostrar notas: mostrará todas las notas del usuario
-borrar notas: preguntará cuál queremos borrar
'''
from Usuarios import acciones

print("""
      Acciones Disponibles:
        -Registro
        -Login
      """)
accion = input("Que quieres hacer?: ")
comando_reconocido = False

haz_el = acciones.Acciones()

while not comando_reconocido:
    if accion.capitalize() == "Registro":
        comando_reconocido = True
        haz_el.registro()
        
    elif accion.capitalize() == "Login":
        comando_reconocido = True
        haz_el.login()
        
    else:
        print("No te he entendido")
        accion = input("Que quieres hacer?: ")
