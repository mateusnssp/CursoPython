"""Manipulação de listas"""


lista =    [7, 5, 6, 2, 3, 1, 8, 4, 9, 0]
# índices:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9

"""Alteração dos respectivos índices"""
lista[0] = 3
lista[0] = lista[2]

"""
Fatiamento:
list[start = 0 : end = 0 : step = 1]
"""
lista_fatiada = [lista[:5]]
lista_fatiada2 = [lista[5:]]
lista_fatiada3 = [lista[3:8]]
lista_fatiada4 = [lista[0::2]]

print(lista_fatiada)
print(lista_fatiada2)
print(lista_fatiada3)
print(lista_fatiada4)
