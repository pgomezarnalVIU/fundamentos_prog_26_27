import numpy as np

# Generamos 5 temperaturas entre 0 y 100, incluidos ambos extremos.
temperaturas = np.linspace(0, 100, 5)

# Convertimos el ndarray de NumPy en una lista de Python.
celsius = temperaturas.tolist()

# Creamos una lista con las temperaturas en Fahrenheit.
# fahrenheit = [temperatura * 9 / 5 + 32 for temperatura in celsius]
fahrenheit = []
for temperatura in celsius:
    fahrenheit.append(temperatura * 9 / 5 + 32)

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)