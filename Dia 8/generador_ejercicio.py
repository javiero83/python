
# def num_infinito():
#     n = 1
#     while True:
#         yield n
#         n += 1
#
# generador = num_infinito()
#
# print(next(generador))
# print(next(generador))

# def multiplos_7():
#     b = 7
#     i = 1
#     while True:
#         n = b * i
#         yield n
#         i += 1
#
#
#
# generador = multiplos_7()
#
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))

def vidas_restantes():
    for v in range(3,-1,-1):
        if v > 1:
            yield f'Te quedan {v} vidas'
        elif v == 1:
            yield f'Te queda {v} vida'
        else:
            yield f'Game Over'


perder_vida = vidas_restantes()

for mensaje in vidas_restantes():
    print(mensaje)
