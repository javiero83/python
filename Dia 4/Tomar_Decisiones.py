from unicodedata import digit

x = False

if x:
    print('Es correcto')
else:
    print('No es correcto')

pet = 'bird'

if pet == 'cat':
    print('You have a cat')
elif pet == 'dog':
    print('You have a dog')
else:
    print('I don\'t know')


edad = 16
calificacion = 9

if edad < 18:
    print('eres menor de edad')
    if calificacion > 7:
        print('Aprobado en la escuela')
    else:
        print('No Aprobado en la escuela')
else:
    print('eres adulto')