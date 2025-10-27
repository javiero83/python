from pathlib import Path

base = Path.home()
#
# guia = Path(base,"Barcelona", "Sagrada_Familia")
#
# print(base)
# print(guia)
#
#

# guia = Path(base, "Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
# #
# print(base)
# print(guia)
# #
# print(guia.parent)
# print(guia.parent.parent)
# print(guia.parent.parent.parent)
# print(guia.parents[2])

# guia = Path(Path.home(),"Europa")
#
# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)
# # la salida son todos los .txt que esten bajo europa, en distintas carpetas

#RELATIVE TO

guia = Path('Europa','España', 'Barcelona', 'Sagrada_Familia.txt')
#
en_europa = guia.relative_to(Path("Europa"))
print(en_europa)
#
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_espania)