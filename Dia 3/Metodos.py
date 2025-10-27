texto = "Este es el texto de Federico"

res1 = texto
res2 = texto.upper()
res3 = texto[2].upper()
res4 = texto.lower()
res5 = texto.split() #toma por defecto de separador el espacio vacio
res6 = texto.split("t")

a = "aprender"
b = "python"
c = "es"
d = "genial"
e= "-".join([a,b,c,d])

res7 = texto.find("g") #cuando find no encuentra nada, usa "-1"
res8 = texto.replace("e","x")


print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(e)
print(res7)
print(res8)