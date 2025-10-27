from pathlib import Path, PureWindowsPath

# carpeta = Path('C:/Users/javier.ortiz/Desktop/Alternativo')
# archivo = carpeta / 'otro_archivo.txt'
#
# mi_archivo = open(archivo)
# print(mi_archivo.read())

carpeta = Path('C:/Users/javier.ortiz/PycharmProjects/PythonProject/Dia 6/test.txt')

#Pathlib no usa "abrir" o "cerrar" el archivo
print(carpeta.read_text())

#nombre archivo
print(f'Nombre archivo: {carpeta.name}')

#suffix
print(f'Sufijo, tipo de archivo: {carpeta.suffix}')


if not carpeta.exists():
    print('Este archivo no existe')
else:
    print("Genial, existe")

#PureWindowsPath = cambia la ruta a tipo windows

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)