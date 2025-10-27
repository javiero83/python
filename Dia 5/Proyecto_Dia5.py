
#Ahorcado

# 1 Crear posibles palabras a usar.
# 2 Iniciar juego, pedir primera letra
# 3 Validar letra recibida
# 4 Checar letra recibida en palabra seleccionada

# Si se acaban las vidas, pierde el jugador,

from random import choice

def init_game():

    words = ['perro', 'gato', 'oso']
    attempts = 6

    game_word = choice(words)
    print(game_word)
    spaces = len(game_word)
    spaces_list = []

    while spaces > 0:
        spaces_list.append("_")
        spaces -=1

    print(f'El juego ha iniciado, tu palabra es: {spaces_list} y tienes {attempts} oportunidades.')

    return spaces_list,attempts,game_word

def validar_letra(letra):
    if type(letra) != str:
        print('Error! Solo se aceptan letras :(')
        return False
    return True

def checar_letra(palabra,letra,intentos):

    if palabra.count(letra) == 0:
        intentos = intentos -1
        mensaje = 'Intenta nuevamente, esa letra no existe en la palabra!'
        return intentos, mensaje




def pedir_letra():

    spaces_list, attempts, game_word = init_game()

    letra = input(print('Dame una letra: '))

    if not validar_letra(letra):
        checar_letra()
    else:
        intentos, mensaje = checar_letra(game_word, letra, attempts)
        while intentos >0:
            print(f'{mensaje}, te quedan {intentos} intentos!')
            intentos-=1



pedir_letra()



