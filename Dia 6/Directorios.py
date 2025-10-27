import os

# # ruta = os.chdir('C:\\Users\\javier.ortiz\\Desktop\\Alternativo')
# ruta = os.makedirs('C:\\Users\\javier.ortiz\\Desktop\\Alternativo\\otra')
# #archivo = open('Otro_archivo.txt')
#
# #print(archivo.read())
#
# #archivo.close()

#ruta = 'C:\\Users\\javier.ortiz\\PycharmProjects\\PythonProject\\Dia 6\\test.txt'

#elemento = os.path.basename(ruta)  #entrega el nombre del archivo
#elemento = os.path.dirname(ruta)  #entrega el donde esta el archivo de "ruta"
#elemento = os.path.split(ruta)  #entrega el nombre del archivo y el path del archivo, en forma de tupla  con los dos elementos

#ELIMINAR RUTA
#os.rmdir('C:\\Users\\javier.ortiz\\Desktop\\Alternativo\\otra')

#print(elemento)

otro_archivo= open('C:\\Users\\javier.ortiz\\Desktop\\Alternativo\\otro_archivo.txt')
print(otro_archivo.read())