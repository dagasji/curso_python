import datetime

class FestivalMusical:

    nombre = None

    def __init__(self, nombre, pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical        

    def festival_metodo(self):
        print(f"El mejor festival es: {self.nombre}")

    #Esto seria el equivalente a un tostring
    def __str__(self) -> str:
        return self.nombre + " " + self.pais

    #Los classmethos modifican valores a nivel de la clase y es común a todas las instancias
    @classmethod
    def valor_ticket(cls, valor):
        cls.valor_ticket = valor 

    @staticmethod
    def dia_evento(dia):
        if(dia.weekday() == 5 or dia.weekday() == 6):
            return print("Es fin de semana")
        else:
            print("Es un día laboral")

#Se instancia el objeto
festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')

#Imprimimos el nombre
print(festival1.nombre)

#Invocamos a un método de la clase
festival1.festival_metodo()

#imprimimos el contenido de la clase (str)
print(festival1)

#Se crea el valor del ticket
festival1.valor_ticket(44)

print("Imprimimos el valor de festival1: ", festival1.valor_ticket)

festival2 = FestivalMusical('Benicassim', 'SP', 'Dance')
print("Imprimimos el valor de festival2: ", festival1.valor_ticket)

print("Imprimimos el valor de la clase: ", FestivalMusical.valor_ticket)

dia1 = datetime.date(2021,11,28)

FestivalMusical.dia_evento(dia1)
