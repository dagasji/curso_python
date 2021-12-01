import io

#entrada  = "Primera linea de prueba\n"

#with open('clase5/quijote_modificado.txt','x') as file:
#    file.write(entrada)

#entrada = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho
#tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua,
#rocín flaco y galgo corredor."""

#with open('clase5/quijote_modificado.txt','a') as file:
#    file.write(entrada)

with open('clase5/quijote_modificado.txt','r') as file:
    file.seek(25)
    contenido = file.read(42)
    print(contenido)