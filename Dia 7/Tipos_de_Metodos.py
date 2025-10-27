class Pajaro:

    alas = True #Atributo de clase

    def __init__(self,color,especie):  #constructor, con parametros de instancia
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print('El pajaro mira!')



# piolin = Pajaro('amarillo','canario')
#
# piolin.pintar_negro()
# piolin.volar(50)
# piolin.alas = False
# print(piolin.alas)


# Pajaro.poner_huevos(3)
# Pajaro.mirar()

class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

# perro = Mascota()
#
# perro.respirar()


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


# yamcha = Jugador
# yamcha.revivir()
#
# print(yamcha.vivo)


class Personaje:
    def __init__(self,cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1


# robin = Personaje(10)
#
# print(robin.cantidad_flechas)
# print(robin.lanzar_flecha())
# print(robin.cantidad_flechas)
