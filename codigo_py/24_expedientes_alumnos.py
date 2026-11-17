# Librerias
from email.encoders import encode_noop

import numpy as np
from rich.console import Console
from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm
from rich.table import Table


# Lista expedientes
expedientes_alumnos = []

# Bucle infinito pidiendo un expediente
while True:
    # Pedimos los datos del usuario
    nombre = Prompt.ask("Introduzca el nombre del alumno")
    edad = IntPrompt.ask("Introduzca la edad en años", default=18)
    calificacion_ciencias = FloatPrompt.ask("Introduce la calificacion en el area "
                                            "científica [0-10]", default=5.0)
    calificacion_humanidades = FloatPrompt.ask("Introduce la calificacion en el area "
                                               "humanidades [0-10]", default=5.0)
    calificacion_artistico = FloatPrompt.ask("Introduce la calificacion en el area "
                                             "artistico [0-10]", default=5.0)

    # Generar un diccionario
    expediente = {
        "nombre": nombre,
        "edad": edad,
        "calificacion_ciencias": calificacion_ciencias,
        "calificacion_humanidades": calificacion_humanidades,
        "calificacion_artistico": calificacion_artistico,
        "promedio": (calificacion_ciencias + calificacion_humanidades + calificacion_artistico) / 3
    }

    # Anyadimos a la lista
    expedientes_alumnos.append(expediente)

    # Solicitar continuar
    continuar = Confirm.ask("¿Quires registrar otro expediente?", default=True)
    if not continuar:
        break

# Imprimir una tabla del listado
console = Console()
# titulos_columnas = ["Nombre", "Edad", ...] y utilizar un for
table = Table(show_header=True, header_style="bold green", title="Expedientes alumnos")
table.add_column("Nombre", justify="center")
table.add_column("Edad", justify="center")
table.add_column("Calificación científica", justify="center")
table.add_column("Calificación humanística", justify="center")
table.add_column("Calificación artística", justify="center")
table.add_column("Promedio", justify="center")
for expediente in expedientes_alumnos:
    table.add_row(expediente["nombre"],
                  str(expediente["edad"]),
                  str(expediente["calificacion_ciencias"]),
                  str(expediente["calificacion_humanidades"]),
                  str(expediente["calificacion_artistico"]),
                  str(round(expediente["promedio"], 2)))
console.print(table)

# Guardamos los valores
valores_expedientes_alumnos = []
for expediente in expedientes_alumnos:
    valores_expedientes_alumnos.append([
        expediente["nombre"],
        expediente["edad"],
        round(expediente["calificacion_ciencias"],2),
        round(expediente["calificacion_humanidades"],2),
        round(expediente["calificacion_artistico"],2),
        round(expediente["promedio"],2)
    ])

datos_expedientes_alumnos = np.array(valores_expedientes_alumnos)
np.savetxt("expedientes_alumnos.csv",
           datos_expedientes_alumnos,
           delimiter=",",
           header="Nombre,Edad,Calf Cientifica,Calf Humanidades,Calf Artistico, Promedio",
           fmt="%s",
           encoding="utf-8")
