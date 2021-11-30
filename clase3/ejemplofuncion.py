def hola():
    print("Hola")

def preguntar_nombre():
    nombre = input("¿Cuál es su nombre? ")
    print(f"Hola {nombre}")
    return nombre

resultado = preguntar_nombre()
print(resultado)