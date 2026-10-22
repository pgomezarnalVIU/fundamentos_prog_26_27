# Semaforo
# verde 1
# amarillo 2
# rojo 3
verde = 1
amarillo = 2
rojo = 3

# Estado del semaforo
semaforo = 3

# Bloque de decision
if semaforo == verde:
    print("Esta en verde")
    print("Puedes pasar")
elif semaforo == amarillo:
    print("Esta en amarillo")
    print("Cuidado al pasar")
else:
    print("Esta en rojo")
    print("No puedes pasar")