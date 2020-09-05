def ss(indice=0, desc='', subDesc=''):
    """
    Estrutura  ::    i.n1.n2.n3 : descrição - descrição segunda
    Variáveis  ::   'i'.n1.n2.n3 :   desc   -     subDesc
    """
    listaBase = list(range(10))
    listaString = []
    l = [listaString.append(f'i.{n1}.{n2}.{n3}') for n1 in listaBase for n2 in listaBase for n3 in listaBase]

    strDesc = ": {}".format(desc) if desc != '' else ''
    strSubDesc = "- {}".format(subDesc) if subDesc != '' else ''
    print("{} {} {}".format(listaString[indice], strDesc, strSubDesc))