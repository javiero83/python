lista = [1,2,3,4] # antes de rango

#for numero in lista:
    #print(numero)

#Ahora con "Range"

#for num in range(0,10,2): #no recibe floats
#    print(num)


suma_cuadrados = 0
cuadrado = 0

for num in range(1,16):
    cuadrado = num**2
    suma_cuadrados +=cuadrado

print(suma_cuadrados)