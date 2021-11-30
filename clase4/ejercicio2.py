def preguntar():
    numero = int(input("Introduzca un número:"))

    if (numero % 2 == 0):
        print("El número es par")
    else: 
        print("El número es inpar")

    if(numero % 4 == 0):
        print("El número es múltipo de 4")

preguntar()
