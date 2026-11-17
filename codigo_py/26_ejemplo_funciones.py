# Funciones y parametros
def saludar():
    print("Hola, bienvenido a matrix")
def saludar_persona(nombre):
    print(f"Hola {nombre} bienvenido a matrix")

def sumar(a,b):
    print(a+b)
def sumar_con_respuesta(a,b):
    return a+b
    # print(f"El resultado es {a+b}")
def cuadrados(a):
    resultados = []
    resultados.append(a*a)
    resultados.append(a * a * a)
    return resultados

# Funciones dos parametros donde importa el lugar
def mostrar_datos_alumno(nombre,edad,nacionalidad="Española"):
    print(f"Nombre: {nombre}, Edad: {edad}, Nacionalidad: {nacionalidad}")

# Funcion paso por valor
def modificar_numero(numero):
    numero = numero * 2
    print(numero)

# Ejemplo con una referencia (lista)
def modificar_lista(lista):
    lista.append(4)



# Uso de funciones
saludar()
saludar_persona("Paco")
sumar(5,6)
resultado=sumar_con_respuesta(6,5)
print(resultado)
resultado_cuadrados=cuadrados(6)
print(resultado_cuadrados)

# Uso de funcion con datos alumno
mostrar_datos_alumno(23,"Paco")
mostrar_datos_alumno(edad=23,nombre="Paco")
mostrar_datos_alumno("Noelia",28,"Chilena")

# Uso paso por valor
altura=1.8
modificar_numero(altura)
print(altura)

# Uso por referencia
temperaturas = [2,6,19]
modificar_lista(temperaturas)
print(temperaturas)