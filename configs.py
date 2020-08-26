"""
Automatiza a produção dos índices para as amostras de etapas de execução.
ss(índice, descrição, subdescrição)
"""
def generate(self = None):
    """.generate(quantidade de índices necessários)"""
    lim, quantidade = list(range(10)), range(10)
    string, vl, svl, ssvl = [], lim, lim, lim
    ns = '0'
    for iq in quantidade:
        for ivl in vl:
            for isvl in svl:
                for issvl in ssvl:
                    string.append('i.{}.{}.{}'.format(ns if ivl == 0 else ivl, ns if isvl == 0 else isvl, issvl))
    return string

def ss(ind, desc, subDesc = ''):

    ss = '{} : {} - {}.' if not subDesc == '' else '{} : {}.'

    indi = generate()
    return print(ss.format(indi[ind], str(desc), str(subDesc)))
