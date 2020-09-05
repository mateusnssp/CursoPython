from configs import *

lista =    [7, 5, 6, 2, 3, 1, 8, 4, 9, 0]
# índices:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9

"""{i.1} Alteração dos respectivos índices"""
lista[0] = 3
lista[0] = lista[2]
lista[5] = lista[-3]

ss(0, lista)                             #{i.0}

"""
Fatiamento:
list[start = 0 : end = 0 : step = 1]
"""
lista_fatiada = [lista[:5]]              #{i.1}
ss(1, lista_fatiada)
lista_fatiada2 = [lista[5:]]             #{i.2}
ss(2, lista_fatiada2)
lista_fatiada3 = [lista[3:8]]            #{i.3}
ss(3, lista_fatiada3)
lista_fatiada4 = [lista[0::2]]           #{i.4}
ss(4, lista_fatiada4)

lista[2:5] = ['a', 'b', 'c']             #{1.5}
ss(5, lista)
