# Preguntar sobre la edad y comprobar
while True:
     edad = int(input("Introduce tu edad: "))
     if edad < 0:
       print("La edad no puede ser negativa.")
       continue
     break
print(f"Edad registrada: {edad}")
