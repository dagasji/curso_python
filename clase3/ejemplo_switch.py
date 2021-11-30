def semana(i):
    dias={
        0: 'Domingo',
        1: lunes,
        2: martes
    }

    resultado = dias.get(i)
    return resultado()

def lunes():
    return 'Lunes'

def martes():
    return 'Martes'



print(semana(2))

