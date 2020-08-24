from configs import *
s = Configure.generate(5)

"""Manipulação de listas"""

lista =    [7, 5, 6, 2, 3, 1, 8, 4, 9, 0]
# índices:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9

"""{i.1} Alteração dos respectivos índices"""
lista[0] = 3
lista[0] = lista[2]
lista[5] = lista[-3]

print(ss.format(s[0], lista))

"""
Fatiamento:
list[start = 0 : end = 0 : step = 1]
"""
lista_fatiada = [lista[:5]]              #{i.2}
print(ss.format(s[1], lista_fatiada))
lista_fatiada2 = [lista[5:]]             #{i.3}
print(ss.format(s[2], lista_fatiada2))
lista_fatiada3 = [lista[3:8]]            #{i.4}
print(ss.format(s[3], lista_fatiada3))
lista_fatiada4 = [lista[0::2]]           #{i.5}
print(ss.format(s[4], lista_fatiada4))

