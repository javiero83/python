'''

Clinica General G
Pediatria P
Cardiologia C

Turnos para cada una
'''

def turnos_general():
    for n in range(1,1000):
        yield f'G - {n}'

def turnos_pediatria():
    for n in range(1,1000):
        yield f'P - {n}'
def turnos_cardiologia():
    for n in range(1,1000):
        yield f'C - {n}'

#tengo que crear las intancias de los generadores

g = turnos_general()
p = turnos_pediatria()
c = turnos_cardiologia()

#decorador
def mostrar_turno(func):
    def wrapper(especialidad):
        print("\n"+"="*30)
        print("🗒️ Turno generado: ")
        func(especialidad)
        print("Por favor, espere a ser llamado.")
        print("="*30 + "\n")
    return wrapper

@mostrar_turno
def obtener_turno(especialidad):
    if especialidad == "G":
        print(next(g))
    elif especialidad == "P":
        print(next(p))
    elif especialidad == "C":
        print(next(c))
