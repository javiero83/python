## 1 Pedir frase, parrafo texto del usuario R
## 2. Pedir a usuario que introduzca 3 letras de su eleccion R
## a. Cuantas veces aparece cada letra que inserto R
## b. Cuantas palabras hay en total R
## c. Cual es la primera y la ultima letra del texto R
## d. Invertir el orden de las palabras R
## e. Aparece "python" en la oracion?

import re


frase = input("Introduce la frase que se analizará: ")
letra1 = input("Introduce la primera letra (de 3) de tu eleccion: ")
letra2 = input("Introduce la segunda letra (de 3) de tu eleccion: ")
letra3 = input("Introduce la tercera letra (de 3) de tu eleccion: ")

#print(frase)
#print(letra1, letra2, letra3)

#Pasando la frase a minuscula
frase = frase.lower()
#Convirtiendo las letras a minusculas
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

#cuantas veces aparece cada letra que inserte, en la frase

qtyLetra1 = frase.count(letra1)
qtyLetra2 = frase.count(letra2)
qtyLetra3 = frase.count(letra3)

print(f"La letra {letra1}, aparece {qtyLetra1} veces en la frase.")
print(f"La letra {letra2}, aparece {qtyLetra2} veces en la frase.")
print(f"La letra {letra3}, aparece {qtyLetra3} veces en la frase.")

#cuantas palabras hay en total

#separando por espacios en blanco
palabrasEspacios = re.split(r'\W+', frase)
cantidadPalabras = len(palabrasEspacios)
#print(palabrasEspacios)
print(f'La frase tiene {cantidadPalabras} palabras')

primeraLetra = frase[0]
print(f'La primera letra es: {primeraLetra}')
ultimaLetra = frase[-1]
print(f'La ultima letra es: {ultimaLetra}')

fraseInversa = " ".join(palabrasEspacios[::-1])
print(f'La frase inversa es: {fraseInversa}')

pythonFrase = palabrasEspacios.count("python")

print(f'La palabra "python" aparece {pythonFrase} veces en la frase.')