# Print
print("Hola Pakito")

# Variables str
comilla_simple = 'Hola Pakito'
comilla_doble = "Hola mundo"
comilla_triple = """Esto es un texto largo de varias líneas (2)
de una misma cadena de texto"""
print(comilla_triple)

# Concatenacion
# nombre = "Paco"
nombre = input("Por favor escribe tu nombre:").strip().upper()
print("Por favor dame tus apellidos:")
apellidos = input().strip().upper()
# apellidos = "Gomez Arnal"
nombre_completo = nombre + " " + apellidos
print(nombre_completo)

# Formateo v1
edad = 50
edad_str = str(edad)
concatenar_str_num = nombre_completo + " " + str(edad)
mensaje = "Hola, mi nombre es {} y tengo {} años".format(nombre_completo,edad)
print(concatenar_str_num)
print(mensaje)

# Formateo f-string
mensaje_f_string = f"Hola, mi nombre es {nombre_completo} y tengo {edad} años"
print(mensaje_f_string)