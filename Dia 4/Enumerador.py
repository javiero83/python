#Ejemplo de como mostrar indice sin usar enumerador
lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#Ejemplo usando enumerador

lista2 = ['a','b','c']

for item2 in enumerate(lista2):
    print(item2)

#Usando enumerate partiendo en variables

list3 = ['a','b','c']
for indice,item4 in enumerate(list3):
    print(indice,item4)