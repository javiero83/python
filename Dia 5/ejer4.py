# def suma_absolutos(*args):
#     return sum(abs(arg) for arg in args)
#
# res = suma_absolutos(1,2,-3,-1)
#
# print(res)

def numeros_persona(nombre, *nums):
    suma_numeros = sum(nums)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

#Funcion return  "{nombre}, la suma de tus números es {suma_numeros}"

print(numeros_persona('Ikki',75,20,65))