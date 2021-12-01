import io

#fichero = open('clase5/quijote_pg2000.txt', 'r')

#for linea in fichero:
#    print(linea)
#fichero.close()

#Lee los primeros 200 caracteres
with open('clase5/quijote_pg2000.txt', 'r') as file:
    contenido = file.read(200)
    print(contenido)

#Lee la primera linea
#with open('clase5/quijote_pg2000.txt', 'r') as file:
#    contenido = file.readline()
#    print(contenido)

#Lee los parrafos de un fichero
with open('clase5/quijote_pg2000.txt', 'r') as file:
    contenidos = file.readlines(2000)

    for c in contenidos:
        print(c.strip())

