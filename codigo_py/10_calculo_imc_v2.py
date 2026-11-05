"""
Programa que calcula el IMC preguntando el peso y la altura
"""

# Pedir peso y la altura
print("Introduce tu peso en kg:")
peso_str = input() # El input devuelve un STRING
# No puedes hacer "80"/2
# Tengo que transformarlo
peso = float(peso_str) # 80.0/2

print("Introduce tu altura en m:")
altura = float(input())

# Calculamos el imc
imc = peso / (altura ** 2)

# Clasificación del IMC
print(f"Tu IMC es {imc:.2f}")
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9: # imc >= 18.5 and imc < 24.9
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")