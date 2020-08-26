from configs import *
ind = Configure.generate()

s = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7}  #{i...0}
print(ss.format(ind[0], s))

"""{i...1} Type == <class 'set'>"""
print(ss.format(ind[1], type(s)))

"""{i..2.0}Pesquisa dentro do conjunto"""
def i3(num):
    return num in s
print(ss.format(ind[20], i3(4))) #{i..2.0}
print(ss.format(ind[21], i3(8))) #{i..2.1}

s = set('54632877565')
print(ss.format(ind[30], s))     #{i..3.0}

"""{i..4.0} Operações"""
a = set('beija-flor')
b = {'m', 'a', 't', 'e', 'u', 's'}
print(ss.format(ind[40], 'a: {},\n{} b: {}'.format(a, ' '*(len(ind[40]) + ss.count(' ')), b)))
print(ss.format(ind[41], a - b))
print(ss.format(ind[42], a | b))
print(ss.format(ind[43], a & b))
print(ss.format(ind[44], a ^ b))
