# Cálculo del Índice de Masa Corporal (IMC)
# Definición de variables
peso = 80  # en kilogramos
altura = 1.85  # en metros

# Cálculo del IMC
imc = peso / (altura ** 2)
print(imc)
# Clasificación del IMC
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9: # imc >= 18.5 and imc < 24.9
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")