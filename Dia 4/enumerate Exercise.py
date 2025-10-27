
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

lista = list(enumerate(lista_nombres))

for indice,item in lista:
    if item[0] == 'M':
        print(indice)