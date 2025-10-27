
def chequear_3_cifras(numero):
    return numero in range(100, 1000)

suma = 453 + 112

res = chequear_3_cifras(suma)
print(res)

lista_3_cifras = []

def check_3_digits_list(lista):
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

res1 = check_3_digits_list([55,919,6000])
print(res1)

res2 = check_3_digits_list([55,919,600])
print(res2)
