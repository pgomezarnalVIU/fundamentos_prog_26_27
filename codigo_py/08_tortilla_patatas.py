"""
Programa en el que se recoja que ingredientes necesitamos para hacer una tortilla española
"""

# Ingredientes
hay_patatas = False
hay_huevos = False
hay_aceite = False
hay_sal = False

# Pedir los ingredientes
pregunta = "¿Tienes patatas? (s/n): "
# respuesta = input(pregunta)
# respuesta_validada = respuesta.lower()
if input(pregunta).lower() == "s":
    hay_patatas = True
else:
    hay_patatas = False
pregunta = "¿Tienes huevos? (s/n): "
if input(pregunta).lower() == "s":
    hay_huevos = True
pregunta = "¿Tienes aceite? (s/n): "
if input(pregunta).lower() == "s":
    hay_aceite = True
pregunta = "¿Tienes sal? (s/n): "
if input(pregunta).lower() == "s":
    hay_sal = True

# Comprobar si podemos hacer la tortilla
if hay_patatas and hay_huevos and hay_aceite and hay_sal:
    print("!Puedes hacer una tortilla de patatas!")
else:
    print("Falta algún ingrediente")