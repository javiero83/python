from collections import Counter
from collections import defaultdict
from collections import namedtuple

#Counter
numeros = [1,2,2,45,5,4,23,1,2,6,7,3,6,4,32,1,3,3,2,2]
cosas = ['perro','pelota','Perro','perro']

print(Counter(numeros))
print(Counter(cosas))

print(Counter('perrisisisimo'))

serie = Counter([1,2,2,1,2,1,1,1,1,2,3,3,4,5,6,1,1,1])
print(serie.most_common())
print(serie.most_common(1))
print(list(serie))

#defaultdict
mi_dic = {'uno':'verde','dos':'rojo','tres':'azul'}
print(mi_dic['dos'])
#print(mi_dic['cuatro'])   --> mandaria error sin defaultdict
mi_dic = defaultdict(lambda :'nada')
print(mi_dic['gogo'])  #--> nada
print(mi_dic)

#namedtuple
Persona = namedtuple('Persona',['nombre','altura','peso'])
hyoga = Persona('Hyoga',1.77,75)

print(hyoga.nombre)