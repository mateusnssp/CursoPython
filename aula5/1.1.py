"""
Este script mostra qual caractere mais aparece na string
"""

string = 'O rato roeu a roupa do rei de roma'

comparador = 1

for caractere in string:
    if string.count(caractere) > comparador:
        comparador = string.count(caractere)
    print(caractere, string.count(caractere))
