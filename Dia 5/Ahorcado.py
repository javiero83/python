from random import choice

def init_game():
    palabras = ['oso', 'gato','elefante']
    palabra_juego = choice(palabras)
    #print(palabra_juego)
    palabra_espacio = []

    for i in palabra_juego:
        palabra_espacio.append("_")

    # vidas = 5
    vidas = 5

    no_de_letras = len(palabra_juego)

    print(f'La palabra a adivinar tiene {len(palabra_juego)} letras, tienes {vidas} intentos')
    print('\n')
    print('Palabra: ', " ".join(palabra_espacio))

    return palabra_juego, vidas, palabra_espacio

def validar_letra(letra,vidas):
    if not letra.isalpha():
        vidas -= 1
        mensaje = f'{letra} no es una letra valida!, pierdes una vida, te quedan: {vidas} :)'
        # time.sleep(1)
        # sys.stdout.write("\033[F")
        # sys.stdout.write("\033[K")

        return False, mensaje, vidas
    else:
        mensaje = 'Letra valida!'
        return True,mensaje, vidas

def checar_letra(palabra, letra,vidas,palabra_espacio):
    #print("checar letra")
    if palabra.find(letra) == -1:
        vidas -= 1
        mensaje = f'La letra {letra} no existe en la palabra, te quedan {vidas} intentos'
        print(mensaje)
        return vidas, palabra_espacio
        if vidas == 0:
            if "_" in palabra_espacio:
                return print('Has perdido')
    else:
       for i,c in enumerate(palabra):
           if c == letra:
                palabra_espacio[i] = letra
       # if "_" not in palabra_espacio:
       #     print('Felicidades has ganado!!! 🎇🎆🥳🙌🍾')
       return vidas, palabra_espacio

def pedir_letra_init():

    palabra_juego, vidas, palabra_espacio = init_game()
    pedir_letra(vidas,palabra_juego,palabra_espacio)


def pedir_letra(vidas,palabra_juego,palabra_espacio):
    letra = input('Dame la letra: ')
    flag, mensaje, vidas_restantes = validar_letra(letra, vidas)

    if flag == False:
        vidas = vidas_restantes
        print(mensaje)
        if vidas == 0:
            return print("Has perdido!")
        pedir_letra(vidas,palabra_juego,palabra_espacio)

    elif flag == True:
        print(mensaje)
        vidas, palabra_espacio = checar_letra(palabra_juego, letra, vidas, palabra_espacio)
        if not "_" in palabra_espacio:
            print("Palabra: ", " ".join(palabra_espacio))
            return print('Felicidades has ganado!!! 🎇🎆🥳🙌🍾')
        print('Palabra', " ".join(palabra_espacio))
        print ('\n')
        pedir_letra(vidas, palabra_juego, palabra_espacio)





pedir_letra_init()