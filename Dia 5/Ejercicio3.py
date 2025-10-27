import random


def lanzar_moneda():

    #debe decir si es cara o cruz
    #sin argumentos
    moneda = ['cara', 'cruz']
    return random.choice(moneda)


def probar_suerte(opcion, lista):

    #toma dos argumentos
    #el resultado de lanzar moneda
    #lista_numeros
    if opcion == 'cara':
        lista.clear()
        return f'La lista se autodestruirá', lista
    else:
        return f'La lista fue salvada', lista


lista_numeros = [1,2,3,4,5]
print(probar_suerte(lanzar_moneda(),lista_numeros))