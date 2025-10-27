mi_tuple = 1,2,3,4 #con o sin parentesis

print(type(mi_tuple))


print(mi_tuple[-2]) #Buscar info en la tupla
#mi_tuple[0] = 5 -> manda error

t = 1,2,(10,20),4

print(type(t))
print(t[2][0])
mi_tuple = list(mi_tuple)

print(type(mi_tuple))

#####################################
## Asignar el contenido de un tuple a distintas variables

t1 = (1,2,3,1)
x,y,z,a = t1

print(x,y,z)

print(len(t1))
print(t1.count(1)) #cuantos 1's hay en el tuple

print(t1.index(2))