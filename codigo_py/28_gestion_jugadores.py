# Librerias
from rich import print
from rich.prompt import Prompt,IntPrompt
from rich.table import Table
from rich.console import Console


# Diccionario con 12 jugadores de basket
plantilla_basket = {
    "1": {"Nombre": "Juan", "Posicion": "Base", "Edad": 25, "Altura": 1.85, "Puntos": 0},
    "2": {"Nombre": "Pedro", "Posicion": "Escolta", "Edad": 28, "Altura": 1.90, "Puntos": 0},
    "3": {"Nombre": "Luis", "Posicion": "Alero", "Edad": 27, "Altura": 1.95, "Puntos": 0},
    "4": {"Nombre": "Carlos", "Posicion": "Ala-Pívot", "Edad": 30, "Altura": 2.00, "Puntos": 0},
    "5": {"Nombre": "Miguel", "Posicion": "Pívot", "Edad": 29, "Altura": 2.05, "Puntos": 0},
    "6": {"Nombre": "Javier", "Posicion": "Base Suplente", "Edad": 24, "Altura": 1.80, "Puntos": 0},
    "7": {"Nombre": "Sergio", "Posicion": "Escolta Suplente", "Edad": 26, "Altura": 1.88, "Puntos": 0},
    "8": {"Nombre": "Andrés", "Posicion": "Alero Suplente", "Edad": 27, "Altura": 1.92, "Puntos": 0},
    "9": {"Nombre": "Fernando", "Posicion": "Ala-Pívot Suplente", "Edad": 31, "Altura": 2.02, "Puntos": 0},
    "10": {"Nombre": "Roberto", "Posicion": "Pívot Suplente", "Edad": 28, "Altura": 2.08, "Puntos": 0},
    "11": {"Nombre": "Alberto", "Posicion": "Base de Reserva", "Edad": 23, "Altura": 1.82, "Puntos": 0},
    "12": {"Nombre": "Diego", "Posicion": "Escolta de Reserva", ("Edad"): 25, "Altura": 1.89, ("Puntos"): 0},
}


# Creamos un funcion que añade puntos a un jugador
# param jugador: nombre dentro de la plantilla
# param puntos: puntos del jugador
def anyadir_puntos(jugador, puntos):
    if jugador in plantilla_basket:
       plantilla_basket[jugador]["Puntos"] += puntos
       print(f"[green]Se han añadido {puntos} al {jugador}[/]")
    else:
        print(f"[red]El jugador {jugador} no esta en el plantilla[/]")

# Funcion que muestre el interfaz sobre los puntos de los jugadores
def menu_anyadir_puntos():
    jugadores_elegibles = list(plantilla_basket.keys())
    jugador_elegido = Prompt.ask("Elige un jugador para añadirle puntos",choices=jugadores_elegibles)
    puntos_anotados = IntPrompt.ask(f"¿Cuantos puntos ha anotado {jugador_elegido}?")
    anyadir_puntos(jugador_elegido, int(puntos_anotados))

def mostrar_plantilla():
    tabla_jugadores = Table(title="Plantilla de jugadores")
    tabla_jugadores.add_column("Numero")
    tabla_jugadores.add_column("Posicion")
    tabla_jugadores.add_column("Puntos")
    for jugador in plantilla_basket:
        tabla_jugadores.add_row(plantilla_basket[jugador]["Nombre"],
                                plantilla_basket[jugador]["Posicion"],
                                str(plantilla_basket[jugador]["Puntos"]))

    Console().print(tabla_jugadores)


# Programa principal
# Cremos un bucle infinito
while True:
    menu_anyadir_puntos()
    salir = Prompt.ask("¿Salir del programa?",choices=["si","no"])
    if salir == "si":
        break

mostrar_plantilla()