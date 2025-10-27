
#
# archivo = open("mi_archivo.txt",'w')
# archivo.write('Nuevo texto')
# archivo.close()
#
# archivo = open("mi_archivo.txt")
# print(archivo.read())
# archivo.close()
#
# archivo = open("mi_archivo.txt",'a')
# archivo.write("Nuevo inicio de sesión")
# archivo.close()
#
# archivo = open("mi_archivo.txt")
# print(archivo.read())
# archivo.close()
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('registro.txt','a')
for r in registro_ultima_sesion:
    archivo.writelines(r + '\t')
archivo.close()

archivo = open('registro.txt')
print(archivo.read())
archivo.close()

