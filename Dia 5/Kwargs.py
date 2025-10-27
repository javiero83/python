# def suma(**kwargs):
#     res = 0
#
#     for clave, valor in kwargs.items():
#         print(f"{clave} = {valor}")
#         res += valor
#     return res
#
# print(suma(x=3,y=5,z=2))

# def prueba(num1, num2, *args, **kwargs):
#
#     print(f'el primer valor es: {num1}')
#     print(f'el segundo valor es: {num2}')
#
#     for n in args:
#         print(f'valor = {n}')
#
#     for clave,valor in kwargs.items():
#         print(f'{clave} = {valor}')
#
#
# prueba(1,2,3,4,5,y=1,z=2,d=2)