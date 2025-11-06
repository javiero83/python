"""
Crear turnero para farmacia
tiene 3 areas:
    - perfumeria
    - farmacia
    - cosmeticos

1. A que area se dirige?
2. Un turno por area
3. Vuelve a sacar turno (siguiente cliente)
4, Llevar el contador de que area de turno dio para cada area   (generador)
5. Tu turno muestra texto: Su turno es: <TURNO> "Aguarde y sera atendido" (decorador)
6. Modulos:
    - numeros.py (generadores, decoradores)
    - principal.py (funciones)
    *** import numeros.py en principal.py

"""
# opcion = ''
# while opcion != 'S':
#     print('*******************')
#     print('TURNOS FARMACIA SOL')
#     print('Opciones:')
#     print('[P] Perfumeria\n[F] Farmacia\n[C] Cosmeticos\n[S] Salir')
#     opcion = input('Seleccione la opción para generar su turno: ').upper()

import numeros

def preguntar():

    print("Bienvenidos a Farmacia Python")

    while True:
        print('[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica')
        try:
            mi_rubro = input('Elija su rubro: ').upper()
            ["P","F","C"].index(mi_rubro) #si lo que elije el usuario no es algo de esa lista mandara error
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break
    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()