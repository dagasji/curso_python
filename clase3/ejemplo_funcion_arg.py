def calcular_media(*args):
    total = 0
    for i in args:
        print(i)
        total += i
    resultado_media = total / len(args)    
    return resultado_media

#primero creamos 3 variables
a, b, c = 5, 2, 10
resultado = calcular_media(a, b, c)
print(f"Media {resultado}")

#probamos a crear tambien un array
lista = {3,2,5}
resultado = calcular_media(*lista)
print(f"Media {resultado}")
