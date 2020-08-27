from configs import *

def fun():
    return

ss(0, type(fun)) #{i.0.0.0} : Type
ss(1, fun(), 'Retorno padrão') #{i.0.0.1} : Retorno padrão

def g(var = None):
    return var
def f():
    return g
def fun():
    return f

ss(2, fun()()(), "fun() retorna f() que retorna g()") #{i.0.0.2}
