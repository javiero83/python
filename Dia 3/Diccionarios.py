diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)

res = diccionario['c1']
print(res)

##############################

cliente = {'nombre':'Ikki','apellido':'fenix','peso':60,'talla':1.76}

consulta = cliente['apellido']
print(f'Apellido: {consulta}')


#########################

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3']['s2'])

###############################################
#EJERCICIO
dic1 = {'c1':['a','b','c'],'c2':['d','e','f']}
#EJERCICIO IMPRIMIR LETRA E MAYUSCULA

print(dic1['c2'][1].upper())

##########################################
# Agregar elementos
dic2 = {1:'a',2:'b'}
print(dic2)
#para agregarle un valor al diccionario
dic2[3] = 'c'
print(dic2)

dic2[2] = 'B'
print(dic2)

#conocer todas las claves
print(dic2.keys())

print(dic2.values())

print(dic2.items())


mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])