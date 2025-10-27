# def mayuscula(texto):
#     print(texto.upper())
#
# def minuscula(texto):
#     print(texto.lower())

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return  otra_funcion

#@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

#@decorar_saludo
def minusculas(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayusculas)

mayusculas('fede')

mayuscula_decorada('ikki')