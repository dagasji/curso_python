import fnmatch
import os

patron = 'ejercicio*'
print("Patron: ", patron)

ficheros = os.listdir("./clase4")
for nombre in ficheros:
    print('Nombre %-30s %s' %(nombre, fnmatch.fnmatch(nombre, patron)))
