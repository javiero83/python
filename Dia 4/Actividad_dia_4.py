from random import *

#
#1. Pregunta usuario nombre
#2. Adivina numero del 1 al 100 (8 intentos)
#3. Respuestas posibles 4  (si la respuesta esta entre -1 o mayor a 100 le dira que eso no es posible,
# Si el numero elegido es menor al secreto, le dira que es menor
# Si el numero elegido es mayor al secreto, le dira que es mayor
#Si el numero es correcto, le dira que acerto y cuantos intentos uso
#Si el numero no es correcto ademas de decirle si es mayor a o menor le pedira otro numero nuevo para seguir adivinando.

intentos = 3
nombre = input("Escribe tu nombre: ")
print(f"Bienvenid@ {nombre}, al juego de adivinar el numero!")
print(f'''Tienes {intentos} intentos para adivinar el numero el cual va de 1 a 100
Buena Suerte!!''')

#Arrancando juego
#Calculando numero a adivinar
num = randint(1,100)
print(num)

restantes = 1


while intentos > 0:
    res = int(input('Dame el numero que crees es el correcto: '))
    if res == num:
        print(f"Correcto! el numero es {res}, solo usaste {restantes} intentos!")
        break
    elif res < 0 or res > 100:
        print(f"El numero que tienes que adivinar esta entre 1 y 100!, te quedan {intentos-1} intentos!")
        intentos -= 1
        restantes += 1
    elif res < num:
        print(f"El numero que elegiste, es MENOR al numero secreto, te quedan {intentos-1} intentos!")
        intentos -=1
        restantes += 1
    elif res > num:
        print(f"El numero que elegiste, es MAYOR al numero secreto, te quedan {intentos - 1} intentos!")
        intentos -= 1
        restantes += 1

if intentos == 0:
    print("Gracias por jugar!")



