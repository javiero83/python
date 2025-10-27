mi_set = set([1,2,3,4,5,(1,1,1)])

print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)


#######################################
print(mi_set)

s = set([1,2,3,4,5])

print(len(s))
print(2 in s)

####################################

s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2)
print(s3)

s1.add(4)
s1.add('s')
print(s1)

s1.discard(6)
print(s1)

s1.remove(3)
print(s1)

sorteo =s2.pop()

print(sorteo)

s1.clear()
print(s1)



