from configs import *

def fun(*args):      #{i.0.0.0}
    return args

result1 = fun(0, 1, 2, 3, 4, 5, 6, 7) # passando args
ss(0, result1, "(*)args para tratar argumentoss soltos")

def fun(**kwargs):    #{i.0.0.1}
    return kwargs

result2 = fun(a = 1, b = 2, c = 3)
ss(1, result2, "(**)kwargs para tratar argumentos definidos")

def fun(m, *args, p = 'padrão', **kwargs):
    return (m, p, args , kwargs)

result3 = fun(0, 1, 2, 3, 4, a = 1, b = 2)
ss(2, result3, 'junção')
