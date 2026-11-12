# A partir de una tupla de alergenos
# decidir si plato contiene alguno

from rich import print
from rich.prompt import Prompt

# Creamos una tupla con algunos alergenos
alergenos = ("gluten", "crustáceos", "huevo", "frutos secos", "lácteos",
             "sulfitos", "pescados", "cacahuetes", "soja")

# Imprimimos la lista
print("[bold magenta]Lista de alergenos[/bold magenta]")
for alergeno in alergenos:
    print(f"[bold cyan]{alergeno}[/bold cyan]")

# Preguntamos al usuario por un plato
plato_favorito = Prompt.ask("[bold blue] Introduce tu plato favorito [/bold blue]")
ingredientes = []

# Preguntamos al usuario por cada uno de los ingredientes
while True:
    ingrediente = Prompt.ask(f"[bold blue]Introduce un ingrediente de {plato_favorito}"
                             f". Introduce fin para finalizar[/]")
    if ingrediente.lower() == "fin":
        break
    ingredientes.append(ingrediente)

# Comprobar si tenemos algún alergeno
alergeno_encontrado = False
for ingrediente in ingredientes:
    if ingrediente.lower() in alergenos:
        print(f"[bold red]!CUIDAD! {plato_favorito} contiene el alergeno {ingrediente}[/]")
        alergeno_encontrado = True
    else:
        print(f"[bold green]El {ingrediente} no es un alergeno[/]")
