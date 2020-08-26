class Configure():
    """
    Esta classe automatiza a produção dos índices para as amostras através do .print().
    É necessário chamar o método Configure.generate() para uma variável type <class 'list'>.
    """
    def __init__(self):
        pass

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

    indi = Configure.generate()
    return print(ss.format(indi[ind], str(desc), str(subDesc)))
