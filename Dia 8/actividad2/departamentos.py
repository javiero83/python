import hospital

def solicitar_turno():
    print("Bienvenido al sistema de Turnos Medicos")

    while True:
        print("[G] - Clinica General\n[P] - Pediatria\n[C] - Cardiologia")
        try:
            especialidad = input("Seleccione su especialidad: ").upper()
            ["G","P","C"].index(especialidad)
        except ValueError:
            print("🚫 Opcion invalida, intente de nuevo.")
        else:
            hospital.obtener_turno(especialidad)
            break

def main():
    while True:
        solicitar_turno()
        try:
            continuar = input("Desea sacar oro turno? [S/N]: ").upper()
            ["S","N"].index(continuar)
        except ValueError:
            print("🚫 Ingrese solo S o N")
        else:
            if continuar == "N":
                print("Gracias por su visita. Que tenga un buen dia!")
                break


main()