# Range
range_de_numeros = range(10)
print(range_de_numeros)

for numero in range_de_numeros:
    print(numero)
print(10*"-")

# Ejemplo de range con step
for i in range(1,5,1):
    print(i)
print(10*"-")

for i in range(1,5,2):
    print(i)

# Suma de los 100 primeros pares
suma = 0
for numero in range(2,101,2):
    suma=suma+numero # suma += numer
print(suma)