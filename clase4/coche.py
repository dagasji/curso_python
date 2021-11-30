""" 
    Coche
"""
class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo        
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print('El depósito de gasolina está lleno')
    def conducir(self):
        print(f'El {self.modelo} se está conduciendo.')

    #Método string para pintar el contenido
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}, Nivel de gasolina: {self.nivel_gasolina}"
    
"""
    Clase CocheElectrico
"""
class CocheElectrico(Coche):
    def __init__(self, marca, modelo, tipo, nivel_bateria):
        super().__init__(marca, modelo, tipo)

        self.nivel_bateria = nivel_bateria

    #Sobreescribimos el metodo string del padre
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}, Nivel de bateria: {self.nivel_bateria}"

# Creando las instancias de la clase Coche
objeto_coche = Coche('Ford','Focus', 'Trend')
# Acceder a los atributos de ese objeto
print(objeto_coche.marca)
print(objeto_coche.modelo)
print(objeto_coche.tipo)
print("Nivel gasolina ", objeto_coche.nivel_gasolina)

# Llamando a los métodos de la clase
objeto_coche.gasolina_completo()
print("Nivel gasolina ", objeto_coche.nivel_gasolina)

objeto_coche.conducir()
print(objeto_coche)

#Creamos una nueva instancia del CocheElectrico y pintamos su contenido
coche_electrico = CocheElectrico("Toyota", "Prius", "Electrico",  "30%")
print(coche_electrico)

print(type(coche_electrico))
print(CocheElectrico.__mro__)