import random

def lanzar_dados():

    num1 = random.randint(1,6)
    num2 = random.randint(1,6)

    return num1, num2


def evaluar_jugada(num1,num2):
    suma = num1 + num2

    if suma <= 6:
        return f'La suma de tus dados es {suma}. Lamentable'
    elif suma < 10:
        return f'La suma de tus dados es {suma} Tienes buenas chances'
    else:
        return f'La suma de tus dados es {suma} Parece una jugada ganadora'


d1, d2 = lanzar_dados()
mensaje = evaluar_jugada(d1,d2)

print(f'Dados: {d1} y {d2}')
print(mensaje)