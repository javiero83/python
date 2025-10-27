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
from numeros import turno_decorador, turno_generador


def main():
    opcion = '0'
    while opcion != '4':
        print('*******************')
        print('TURNOS FARMACIA SOL')
        print('Opciones:')
        print('[1] Perfumeria\n[2] Farmacia\n[3] Cosmeticos\n[4] Salir')
        opcion = input('Seleccione la opción para generar su turno: ')

        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass


main()