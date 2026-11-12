# Vamos a realizar una ficha de un jugador de baloncesto
# Pedir datos: nombre, edad, altura y posicion
# Usaremos rich

from rich.console import Console
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich.table import Table

# Generamos una instancia Console
console = Console()

# Pedir al usuario que introduzca los datos del jugador de basket
nombre = Prompt.ask("Introduce el nombre del jugador")
edad = IntPrompt.ask("Introduce la edad del jugador (en años)", default=18)
altura = FloatPrompt.ask("Introduce la altura del jugador (en metros)", default=1.80)
posicion = Prompt.ask("Introduce la posicion del jugador", choices=["Base", "Escolta",
                                                                    "Alero", "Ala-pivot", "Pivot"])

# Sacar los datos en una tabla
table = Table(title="Ficha del jugador")
table.add_column("Campo", style="cyan")
table.add_column("Valor", style="magenta")

table.add_row("Nombre", nombre)
table.add_row("Edad", str(edad))
table.add_row("Altura", str(altura))
table.add_row("Posición", posicion)

console.print(table)
