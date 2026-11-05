from rich import print

# Lista de nombres
nombres_alumnos = ["Ana", "Rocio", "Abraham", "Carlos"]

# Bucle sobre nombres_alumnos
for nombre in nombres_alumnos:
    print(nombre.upper())

print(10*"-")

# lista de temperaturas
temperaturas = [10, 30, 13, 4, 23, 6, -1, 8, 9, 10]
for temperatura in temperaturas:
    print(temperatura)
    if temperatura <= 0:
        print("[bold red]ERROR EN LA TEMPERATURA[/bold red]")
        break

print(10*"-")
print(temperaturas)

# Ejemplo de continue
numeros = [1,2,3,4,-5,56,6,7,8,9,9]
positivos = []
for n in numeros:
  if n<0:
    print("No es positivo")
    continue
  else:
    positivos.append(n)

print(positivos)