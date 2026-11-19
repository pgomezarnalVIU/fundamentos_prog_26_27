import pandas as pd

# Crear DataFrame a partir de un diccionario
data = {
    "Nombre": ["Paco", "Juan", "Ana", "Luis"],
    "Edad": [45, 50, 24, 62]
}

df = pd.DataFrame(data)

# Imprimimos el Dataframe
print(df)