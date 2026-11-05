# Ingredientes
hay_patatas = False
hay_huevos = False
hay_aceite = False
hay_sal = False

# Lista de la compra
lista_compra = []

# Pedir los ingredientes
pregunta = "¿Tienes patatas? (s/n): "
if input(pregunta).lower() == "s":
    hay_patatas = True
else:
    hay_patatas = False
    lista_compra.append("patatas")

pregunta = "¿Tienes huevos? (s/n): "
if input(pregunta).lower() == "s":
    hay_huevos = True
else:
    hay_huevos = False
    lista_compra.append("huevos")

pregunta = "¿Tienes aceite? (s/n): "
if input(pregunta).lower() == "s":
    hay_aceite = True
else:
    hay_aceite = False
    lista_compra.append("aceite")

pregunta = "¿Tienes sal? (s/n): "
if input(pregunta).lower() == "s":
    hay_sal = True
else:
    hay_sal = False
    lista_compra.append("sal")

# Comprobar si podemos hacer la tortilla
if hay_patatas and hay_huevos and hay_aceite and hay_sal:
    print("!Puedes hacer una tortilla de patatas!")
else:
    print("Falta algún ingrediente")
    print(lista_compra)