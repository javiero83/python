from collections import Counter


def reducir_lista(lista):

    counts = Counter(lista)
    reducida = list(counts.keys())

    #encontrar mayor
    mayor = max(reducida)

    #eliminarlo
    reducida.remove(mayor)
    # print(reducida)

    return reducida

def promedio(lista):

    prom = sum(lista)/len(lista)

    return prom



reducida1 = reducir_lista([1,2,2,3,3,4,4,1,5,7,6])
print(promedio(reducida1))