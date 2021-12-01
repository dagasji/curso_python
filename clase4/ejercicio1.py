import datetime

class Ejercicio1():
    
    nombre = None
    edad = None
    
    def preguntar(self):
        self.nombre = input("Introduzca el nombre: ")
        self.edad = int(input("Introduzca la edad: "))

    def calcular(self):
        currentDate = datetime.date.today()
        anio_actual = currentDate.year
        anio_100 = anio_actual + (100 - self.edad)
        print(f"Cumplirá los 100 años en el año {anio_100}")


ejercicio = Ejercicio1()
ejercicio.preguntar()
ejercicio.calcular()
