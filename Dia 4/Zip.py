
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,49,42]
ciudades = ['Lima','Madrid','Mexico']

#Integrar en una tupla usando zip

combinados = list(zip(nombres, edades,ciudades))

print(combinados)

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')