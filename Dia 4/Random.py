#importar metodos en python

#from random import randint
from random import *  #asi importas todo el contenido de la libreria

aleatorio = randint(1,50)
print(aleatorio)

aleatorioU = uniform(1,5)
print(aleatorioU)

#redondeando el numero a 1 decimal
aleatorioDecimal = round(uniform(1,5),1)
print(aleatorioDecimal)

aleato = random()
print(aleato)

colores = ['azul', 'rojo', 'verde','amarillo']
aleatorioLista = choice(colores)
print(aleatorioLista)

#shuffle -> mezclar
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)