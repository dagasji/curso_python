def preguntar():
    nombre = input("Introduzca el nombre: ")
    edad = int(input("Introduzca la edad: "))

    anio_100 = 2021 + (100 - edad)
    print(f"Cumplirá los 100 años en el año {anio_100}")

preguntar()