import numpy as np


# Colecciones
lista = [1,2,2,4,5,6,7,8,8,8]
segunda_lista = [4,5,2,7,4,1,2,1]
tupla = (1,2,3,4,5,6,7,8,9,10)
sets = {1,2,3,4,5,6,7,8,9,10}

# Crear sets a partir de otras colecciones
set_from_lista = set(lista)
print(set_from_lista)

# Modificar las colecciones
lista.append(10)
# tupla no puedo añadir
sets.add(10)
print(sets)

# Eliminar un elemento
set_from_lista.remove(4)

# Ordenar lista
print(segunda_lista)
segunda_lista.sort()
print(segunda_lista)

# Creamos np a partir de una lista
datos = np.array(lista)
np.savetxt('datos_v2.csv', datos, delimiter=';')