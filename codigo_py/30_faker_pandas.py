# Librerias
from faker import Faker

# Configuramos el idioma
fake = Faker("es_ES")

# lista alumnos
alumnos = []

# Generamos 100 alumnos
# _ significa que no definimos ninguna variable de uso
for _ in range(100):
    alumno = {
        "Nombre" : fake.first_name(),
        "Apellido" : fake.last_name(),
        "Edad" : fake.random_int(min=18, max=100),
        "Correo electronico" : fake.email(),
        "Direccion" : fake.address(),
        "Telefono" : fake.phone_number(),
    }
    alumnos.append(alumno)

