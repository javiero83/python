class Pajaro:

    alas = True #Atributo de clase

    def __init__(self,color,especie):  #constructor, con parametros de instancia
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio mi color es {}".format(self.color))

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')


# piolin = Pajaro('amarillo','canario')
#
# piolin.piar()
# piolin.volar(50)

class Perro:

    def ladrar(self):
        print('Guau!')


# akira = Perro()
# akira.ladrar()


class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')

# merlin = Mago()
# merlin.lanzar_hechizo()

class Alarma():

    def postergar(self,cantidad_minutos):
        print('La alarma ha sido pospuesta {} minutos'.format(cantidad_minutos))

# ala = Alarma()
# ala.postergar(10)
