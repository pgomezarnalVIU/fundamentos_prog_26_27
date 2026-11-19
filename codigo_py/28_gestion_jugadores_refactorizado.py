# Librerias
from rich import print
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.console import Console

# Diccionario con 12 jugadores de basket
posiciones_jugadores = ("Base", "Escolta", "Alero", "Ala-pivot", "Pivot")
plantilla_basket = [
    {"Nombre": "Juan", "Dorsal": 0, "Posicion": posiciones_jugadores[0], "Edad": 25, "Altura": 1.85, "Puntos": 0},
    {"Nombre": "Pedro", "Dorsal": 10, "Posicion": posiciones_jugadores[1], "Edad": 28, "Altura": 1.90, "Puntos": 0},
    {"Nombre": "Luis", "Dorsal": 21, "Posicion": posiciones_jugadores[2], "Edad": 27, "Altura": 1.95, "Puntos": 0},
    {"Nombre": "Carlos", "Dorsal": 33, "Posicion": posiciones_jugadores[3], "Edad": 30, "Altura": 2.00, "Puntos": 0},
    {"Nombre": "Miguel", "Dorsal": 15, "Posicion": posiciones_jugadores[4], "Edad": 29, "Altura": 2.05, "Puntos": 0},
    {"Nombre": "Javier", "Dorsal": 45, "Posicion": posiciones_jugadores[0], "Edad": 24, "Altura": 1.80, "Puntos": 0},
    {"Nombre": "Sergio", "Dorsal": 46, "Posicion": posiciones_jugadores[1], "Edad": 26, "Altura": 1.88, "Puntos": 0},
    {"Nombre": "Andrés", "Dorsal": 49, "Posicion": posiciones_jugadores[2], "Edad": 27, "Altura": 1.92, "Puntos": 0},
    {"Nombre": "Fernando", "Dorsal": 62, "Posicion": posiciones_jugadores[3], "Edad": 31, "Altura": 2.02, "Puntos": 0},
    {"Nombre": "Roberto", "Dorsal": 74, "Posicion": posiciones_jugadores[4], "Edad": 28, "Altura": 2.08, "Puntos": 0},
    {"Nombre": "Alberto", "Dorsal": 78, "Posicion": posiciones_jugadores[0], "Edad": 23, "Altura": 1.82, "Puntos": 0},
    {"Nombre": "Diego", "Dorsal": 100, "Posicion": posiciones_jugadores[1], ("Edad"): 25, "Altura": 1.89,
     ("Puntos"): 0},
]


# Creamos un funcion que añade puntos a un jugador
# param jugador: nombre dentro de la plantilla
# param puntos: puntos del jugador
def anyadir_puntos(jugador, puntos):
    if jugador in range(0, len(plantilla_basket)):  # plantilla_basket[jugador], plantilla_basket[3]
        plantilla_basket[jugador]["Puntos"] += puntos
        print(f"[green]Se han añadido {puntos} al {jugador}[/]")
    else:
        print(f"[red]El jugador {jugador} no esta en el plantilla[/]")


# Funcion que muestre el interfaz sobre los puntos de los jugadores
def menu_anyadir_puntos():
    # jugadores_elegibles = []
    # for i in range(0,len(plantilla_basket)):
    #    jugadores_elegibles.append(str(i))
    jugadores_elegibles = [str(i) for i in range(0, len(plantilla_basket))]
    jugador_elegido = Prompt.ask("Elige un jugador para añadirle puntos", choices=jugadores_elegibles)
    puntos_anotados = IntPrompt.ask(f"¿Cuantos puntos ha anotado {jugador_elegido}?")
    anyadir_puntos(int(jugador_elegido), int(puntos_anotados))


def mostrar_plantilla():
    tabla_jugadores = Table(title="Plantilla de jugadores")
    tabla_jugadores.add_column("Numero")
    tabla_jugadores.add_column("Dorsal")
    tabla_jugadores.add_column("Posicion")
    tabla_jugadores.add_column("Puntos")
    for jugador in range(0, len(plantilla_basket)):
        tabla_jugadores.add_row(plantilla_basket[jugador]["Nombre"],
                                str(plantilla_basket[jugador]["Dorsal"]),
                                plantilla_basket[jugador]["Posicion"],
                                str(plantilla_basket[jugador]["Puntos"]))

    Console().print(tabla_jugadores)


# Programa principal
# Cremos un bucle infinito
while True:
    menu_anyadir_puntos()
    salir = Prompt.ask("¿Salir del programa?", choices=["si", "no"])
    if salir == "si":
        break

mostrar_plantilla()
