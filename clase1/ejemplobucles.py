ciudades = ["Málaga", "Granada", "Sevilla", "Cordoba"]

print("------Lista original")
for c in ciudades:
    print(c)

print("------Ordenamos")
ciudades.sort()

for c in ciudades:
    print(c)

print("-----Invertimos")
ciudades.reverse()

for c in ciudades:
    print(c)

##pruebas de diccionarios
frutas = {'manzana': 'roja', 'pera' : 'verde'}

for f in frutas:
    print(f) 

print(frutas['manzana'])


#Operaciones sobre cadenas
cadena = 'Python'
print(cadena[0])

print(len(cadena))

if(len(cadena) > 1):
    print("Es mayor de 1")

if(not len(cadena) > 10):
    print("Es menor de 10")