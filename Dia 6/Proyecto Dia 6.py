#Dia 6
import os
import shutil
from pathlib import Path
from xml.dom.minidom import ProcessingInstruction


recetario_ruta = Path(Path.home(), "Recetas")
opcion = 0

def contar_recetas(archivo):
    count = 0
    for txt in Path(archivo).glob('**/*.txt'):
        count +=1
    return count

def limpiar_consola():
    print("\n"*100)

def obtener_categorias():
    categorias = [carpeta.name for carpeta in recetario_ruta.iterdir() if carpeta.is_dir()]
    return categorias

def mostrar_categorias():
    #print(recetario_ruta)
    lista_cat = obtener_categorias()
    return "\n".join([f"{i+1}. {categoria}" for i, categoria in enumerate(lista_cat)])

def mostrar_recetas_categoria(opcion):

    categorias = obtener_categorias()
    cat_seleccionada = categorias[opcion-1]
    #print(cat_seleccionada)

    nueva_ruta = Path(recetario_ruta,cat_seleccionada)
    print("Recetas Disponibles:")
    i=1
    recetas_lista = []
    for txt in Path(nueva_ruta).glob("**/*.txt"):
        print(f"{i}. {txt.stem}")
        i+=1
        recetas_lista.append((txt.stem))
    if i==1:
        #inicio_programa()
        return nueva_ruta,False
    opc = int(input("\nQue receta usaras? "))

    #print(nueva_ruta, recetas_lista[opc-1])

    return nueva_ruta,recetas_lista[opc-1]

def validar_categoria(nombre):
    #print('validar categoria')
    categorias = obtener_categorias()

    if nombre in categorias:
        return f'Categoria "{nombre}" ya existe!', True
    else:
        return f'Categoria valida!', False

def leer_receta(ruta, opc):
    #folder = ruta
    #nombre = opc

    archivo = Path(ruta) / f"{opc}.txt"

    if archivo.exists():
        contenido = archivo.read_text(encoding='utf-8')
        return contenido
    else:
        return f"El archivo {opc} no existe en {ruta}"

def crear_receta(cat,nombre):
    #print("crear receta")

    categorias = obtener_categorias()
    cat_seleccionada = categorias[cat - 1]

    ruta = recetario_ruta / cat_seleccionada
    ruta.mkdir(parents=True,exist_ok=True)


    archivo = ruta / f'{nombre}.txt'
    mi_archivo = open(archivo,'w',encoding="utf-8")
    receta = input('Escribe el contenido de la receta: ')
    mi_archivo.write(receta)
    mi_archivo.close()
    print("\nReceta Creada")
    return ruta

def crear_categoria(nombre):
    #print('crear categoria')
    ruta = recetario_ruta / nombre
    ruta.mkdir(parents=True,exist_ok=True)
    print('Categoria Creada!')

def eliminar_receta(ruta,opc):
    #print('eliminar receta')
    #folder = ruta
    #nombre = opc

    archivo = Path(ruta) / f"{opc}.txt"

    if archivo.exists():
        archivo.unlink()
        return 'Receta eliminada!'
    else:
        return 'La receta no fue eliminada'

def eliminar_categoria(opc):
    print('eliminar categoria')

    categoria = obtener_categorias()
    cat_seleccionada = categoria[opc - 1]
    folder = cat_seleccionada

    directorio = recetario_ruta / folder
    print(f"Intentando eliminar: {directorio.resolve()}")

    if directorio.exists():
        try:
            shutil.rmtree(directorio)  # elimina incluso si no está vacío
            return f"Categoría '{cat_seleccionada}' y sus recetas eliminadas!"
        except Exception as e:
            return f"No se pudo eliminar la categoría '{cat_seleccionada}': {e}"
    else:
        return f"La categoría '{cat_seleccionada}' no existe!"



def inicio_programa():
    print(f'''
                ********************************************************************************
                Bienvenido a tu recetario 2025
                Las recetas se ubican en la siguiente carpeta: {recetario_ruta}
                Número total de recetas: {contar_recetas(recetario_ruta)}
                ********************************************************************************
                                ''')

    while opcion !=6:
        opc= input('''
        MENU DE RECETARIO (Selecciona la opcion deseada)
        1. Leer Receta
        2. Crear Receta
        3. Crear Categoria
        4. Eliminar Receta
        5. Eliminar Categoria
        6. Finalizar 
        Opcion: ''')

        if opc == '1':
            limpiar_consola()
            print('***LEER RECETA***')
            print(f"Categorias:\n{mostrar_categorias()}")
            cat = int(input("Que categoria quieres consultar? "))
            if cat > len(obtener_categorias()):
                print("Categoria no existente")
            else:
                nueva_rut, opc = mostrar_recetas_categoria(cat)
                if opc != False:
                    limpiar_consola()
                    print(leer_receta(nueva_rut,opc))
                else:
                    print('Esta categoria no tiene recetas disponibles :(')



        elif opc == '2':
            limpiar_consola()
            print('***CREAR RECETA***')
            print(f"Categorias:\n{mostrar_categorias()}")
            cat = int(input("A que categoria pertenece la nueva receta? "))
            if cat > len(obtener_categorias()):
                print("Categoria no existente")
            else:
                nombre = input('Cual es el nombre de la nueva receta?')
                nueva_rut = crear_receta(cat,nombre)
                print(f'Nueva receta creada en: {nueva_rut}')
        elif opc == '3':
            limpiar_consola()
            print('****CREAR CATEGORIA****')
            print('Estas son las categorias actuales: ')
            print(mostrar_categorias())
            nombre = input('Cual es el nombre de la nueva categoria? ')
            mensaje, flag = validar_categoria(nombre)
            if flag == False:
                print(mensaje)
                crear_categoria(nombre)
            elif flag == True:
                print(mensaje)


        elif opc == '4':
            limpiar_consola()
            print('***ELIMINAR RECETA***')
            print(f"Categorias:\n{mostrar_categorias()}")
            cat = int(input("Que categoria quieres consultar? "))
            if cat > len(obtener_categorias()):
                print("Categoria no existente")
            else:
                nueva_rut, opc = mostrar_recetas_categoria(cat)
                print(eliminar_receta(nueva_rut,opc))

        elif opc == '5':
            limpiar_consola()
            print('***ELIMINAR CATEGORIA***')
            print(f"Categorias:\n{mostrar_categorias()}")
            cat = int(input("Que categoria quieres eliminar? "))
            if cat > len(obtener_categorias()):
                print("Categoria no existente")
            else:
                print(eliminar_categoria(cat))

        elif opc =='6':
            print('Programa terminado!')
            return None



inicio_programa()