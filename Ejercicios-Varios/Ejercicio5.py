'''
Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA           DEPORTES
GTA         ASSASINS           FIFA 21
COD         CRASH              PRO 21
PUBG        PRINCE OF PERSIA   MOTO GP 21

Mostrar esta informacion ordenada, primero accion, luego aventura y por ultimo deportes
'''

tabla = [
    {
        "Categoria": "ACCION",
        "Juegos": ["GTA","COD","PUBG"]
    },
    {
        "Categoria": "AVENTURA",
        "Juegos": ["ASSASINS","CRASH","PRINCE OF PERSIA"]
    },
    {
        "Categoria": "DEPORTES",
        "Juegos": ["FIFA 21","PRO 21","MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"------------{categoria['Categoria']}------------")
    for juego in categoria['Juegos']:
        print(juego)