import numpy as np

# Crear un array de 7 elementos entre 0 y 10
array = np.linspace(0, 10, 7)
print(array)

for numero in range(0, 10, 2):
    print(numero)

# Crear un array negativo
array2 = np.linspace(-1, 1, 10)
print(array2)

# Transformar un nparray en una lista
lista = array.tolist()
print(lista)