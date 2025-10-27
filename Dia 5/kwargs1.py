#
# def cantidad_atributos(**kwargs):
#     return len(kwargs)
#
#
#     # print(f'Parametros recibidos: ', kwargs)
#     # print("Cantidad de parametros: ", len(kwargs))
#
#
#
#
# print(cantidad_atributos(x=1,t=2,f=44,g='asa'))


# def lista_atributos(**kwargs):
#     items = list(kwargs.items())
#
#     return items
#
# print(lista_atributos(x=1,f=2))

def describir_persona(nombre, **kwargs):

    print(f'Características de {nombre}:')

    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')



describir_persona("María", color_ojos="azules", color_pelo="rubio")

