
def abrir_leer(archivo):
    arc = open(archivo)
    return arc.read()

def sobrescribir(archivo):
    arc = open(archivo,'w')
    return arc.write('contenido eliminado')

def registro_error(archivo):
    arc = open(archivo,'a')
    return arc.write('se ha registrado un error de ejecución')


print(abrir_leer('test.txt'))