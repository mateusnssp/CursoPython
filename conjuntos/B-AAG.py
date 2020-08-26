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
