from configs import *

s = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7}  #{i...0}
ss(0, s, "estrutura de conjunto")

"""{i...1} Type == <class 'set'>"""
ss(1, type(s), "classe")

"""{i..2.0}Pesquisa dentro do conjunto"""
def i3(num):
    return num in s
ss(20, i3(4))                #{i..2.0}

ss(21, i3(8))               #{i..2.1}

s = set('54632877565')
ss(30, s)                   #{i..3.0}

"""{i..4.0} Operações"""
a = {0, 1, 2, 3, 4, 5, 6}
b = {3, 4, 5, 6, 7, 8, 9}

ss(40, a-b)   #i.0.4.0
ss(41, a | b) #i.0.4.1
ss(42, a & b) #i.0.4.2
ss(43, a ^ b) #i.0.4.3
