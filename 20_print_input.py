# Vamos a rellenar una ficha de un jugador de baloncesto. 
# Para ello, vamos a pedir al usuario que introduzca los siguientes 
# datos: nombre, edad, altura y posición. Una vez que tengamos todos los datos, 
# los imprimiremos en pantalla.

# Pedimos al usuario que introduzca los datos del jugador
nombre = input("Introduce el nombre del jugador: ")
try:
    edad = int(input("Introduce la edad del jugador(en años): "))
except ValueError:
    print("Por favor, introduce un número válido para la edad.")
    edad = int(input("Introduce la edad del jugador(en años): "))
try:
    altura = float(input("Introduce la altura del jugador (en metros): "))
except ValueError:
    print("Por favor, introduce un número válido para la altura.")
    altura = float(input("Introduce la altura del jugador (en metros): "))
posicion = input("Introduce la posición del jugador: ")

# Imprimimos los datos del jugador en pantalla
print("\nFicha del jugador:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print(f"Posición: {posicion}")
