
def suma_menores(numeros):
    res = 0
    for n in numeros:
        if n in range(0, 1000):
            res += n
        else:
            pass
    return res


lista_numeros = [1, 2, 3, 4, 5]

print(suma_menores(lista_numeros))