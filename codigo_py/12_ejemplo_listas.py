# Creamos una lista
frutas = ['manzana','platanos','naranja','naranja'] # Tiene 3 elementos
frutasv2 = ['manzana,platanos,naranja'] # Tiene 1 elemento

# Acceder a un elemento
print(frutas)
print(frutas[0]) # manzana

# Modificar un elemento
frutas[1] = 'peras'
print(frutas)

# Añadir un elemento
frutas.append('uvas')
print(frutas)

# Insertar un elemento en la posicion 1
frutas.insert(1,'platanos')
print(frutas)

# Eliminar un elemento
frutas.remove('naranja') # Elimina la primera ocurrencia del valor
print(frutas)
elemento_eliminado=frutas.pop(0)
print("He eliminado " + elemento_eliminado)
print(frutas)

# Longitud
print(len(frutas))

#print(frutas[len(frutas)]) # error
