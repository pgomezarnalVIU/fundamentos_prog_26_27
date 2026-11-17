from rich.prompt import Prompt, FloatPrompt
from rich import print
from rich.console import Console
from rich.table import Table


# Funcion que calcula el precio final de un producto aplicando
# descuento e IVA
def calcular_precio(precio, descuento, iva=21):
    precio_descuento = precio * (1 - descuento / 100)
    precio_final = precio_descuento * (1 + iva / 100)
    return round(precio_final, 2)


# Bucle principal del programa
precios_productos = []
precios_finales = []
while True:
    # Pregunta por el precio en decimal
    precio = FloatPrompt.ask(
        "Introduce el precio del producto (o '-1' para salir)"
    )
    if precio == -1:
        break

    descuento = FloatPrompt.ask(
        "Introduce el porcentaje de descuento",
        default="0"
    )

    # Pregunta por el IVA en decimal
    iva = FloatPrompt.ask(
        "Introduce el porcentaje de IVA (por defecto 21%)",
        default="21"
    )

    # Conversión a números
    precio = float(precio)
    precios_productos.append(precio)
    descuento = float(descuento)
    iva = float(iva)
    # Llamada con argumentos posicionales
    if iva == 21:
        resultado = calcular_precio(precio, descuento)
    else:
        resultado = calcular_precio(precio, descuento, iva)

    precios_finales.append(resultado)
    print(f"[green]Precio final: {resultado:.2f} €[/green]")

print("[yellow]CALCULOS REALIZADOS[/yellow]")
precios_tabla = Table(title="Precios de productos")
precios_tabla.add_column("Producto", style="cyan")
precios_tabla.add_column("Precio sin iva", justify="right", style="green")
precios_tabla.add_column("Precio con iva", justify="right", style="green")

for i, (precio, precio_final) in enumerate(zip(precios_productos, precios_finales), start=1):
    precios_tabla.add_row(str(i), f"{precio:.2f} €", f"{precio_final:.2f} €")

console = Console()
console.print(precios_tabla)
