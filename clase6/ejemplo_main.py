# -*- coding: utf-8 -*-
# Ejemplo variables __name__ y __main__
# Fichero foo.py
import math

print("Antes import")

print("Antes función A")
def funcionA():
    print("Función A")
    print("Antes función B")
    
def funcionB():
    print("Función B: {}".format(math.sqrt(100)))

print("Antes del control __name__")
if __name__ == '__main__':
    funcionA()
    funcionB()
else:
    print("name: ", __name__)

print("Después del control __name__")