

palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

#comprension de listas

palabra2 = 'python'
lista2 = [letra for letra in palabra2]
print(lista2)

lista3 = [numero for numero in range(0,21,2)]
print(lista3)

lista4 = [num for num in range(0,21,2) if num*2 > 10]
print(lista4)

######################
#transformar la lista de pies a metros
pies = [10,20,30,40,50]
metros = [n/3.281 for n in pies]

print(metros)

