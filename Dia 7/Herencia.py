class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

#comprobando herencia con __bases__

# print(Pajaro.__bases__)
# print(Animal.__subclasses__())
#
# piolin = Pajaro(2,'amarillo')
# piolin.nacer()
# print(piolin.color)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass


# ikki = Alumno('ikki',14)
#
# print(ikki.nombre)
# print(ikki.edad)


class Mascota:

    def __init__(self,edad,nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

# firu = Perro(1,'firu',4)
#
# print(firu.edad)
# print(firu.nombre)
# print(firu.cantidad_patas)

class Vehiculo:

    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass


# tsuru = Automovil()
#
# tsuru.frenar()
# tsuru.acelerar()