# Ficha de jugador de baloncesto
ficha_jugador = {
    "nombre": "TJ Shorts",
    "equipo": "Valencia Basket",
    "altura": 1.75,
    "posicion": "Base",
    "dorsal": 0
}

# Convertir una tupla/lista en un diccionario
# Tupla de datos de un jugador
registro_ficha_jugador = dict (
    [ # Lista
        ('nombre', 'TJ Shorts'), # Tupla
        ('equipo', 'Valencia Basket'),
        ('posicion', 'Base'),
        ('dorsal', 0),
    ]
)

# Imprimir el valor de una clave
print(ficha_jugador['nombre'])
print(registro_ficha_jugador['nombre'])

# Imprimir las claves o los valores
print(ficha_jugador.keys())
print(ficha_jugador.values())

# Imprimir los pares clave-valor
for clave in ficha_jugador:
    print(ficha_jugador[clave])

for clave, valor in ficha_jugador.items():
    print(f"{clave}: {valor}")

# Crear una lista de jugadores donde cada jugador es un diccionario
jugadores_equipo_basket = [
    # Lista
    # Jugador[0]
    {
        # Diccionario
        # Jugador TJ Shorts
        "nombre": "TJ Shorts",
        "equipo": "Valencia Basket",
        "altura": 1.72,
        "posicion": "Base",
        "dorsal": 0,
    },
    # Jugador[1]
    {
        # Diccionario
        # Jugador John Doe
        "nombre": "John Doe",
        "equipo": "Valencia Basket",
        "altura": 1.85,
        "posicion": "Alero",
        "dorsal": 23,
    },
    # Jugador[2]
    {
        # Diccionario
        # Jugador Jane Smith
        "nombre": "Jane Smith",
        "equipo": "Valencia Basket",
        "altura": 1.78,
        "posicion": "Escolta",
        "dorsal": 12,
    }
]

jugador_num_2 = jugadores_equipo_basket[1]
for clave, valor in jugador_num_2.items():
    print(f"{clave}: {valor}")

# Imprimir el nombre del jugador 3
jugador_num3 = jugadores_equipo_basket[2]
# print(jugadores_equipo_basket[2]['nombre'])
print(jugador_num3['nombre'])