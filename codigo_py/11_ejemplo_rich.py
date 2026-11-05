# Importar la funcion print desde la librería rich
from logging import setLogRecordFactory
from socket import create_connection

from rich import print
from rich.console import Console
from rich.table import Table

# Formateo de strings
print("[bold magenta]Buenos días [/bold magenta] soy tu asistente personal")
print("[bold]Me llamo Paco[/bold]")
Console().print("Introduce tu nombre",style="underline magenta")

# Imprimir un a tabla
tabla = Table(title="Lista de la compra",show_lines=True)
tabla.add_column("Producto",style="cyan")
tabla.add_column("Cantidad",justify="right")
tabla.add_row("Huevos","12")
tabla.add_row("Patatas",str(2))
Console().print(tabla)


