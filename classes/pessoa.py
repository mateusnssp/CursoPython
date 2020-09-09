class Pessoa():

    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def apresentar(self):
        self.falar = True
        if not self.comendo:
            print(f'Oi, meu nome é {self.nome} e tenho {self.idade} anos de idade.')
        else:
            print('f{nome} não pode se apresentar pois está comendo.')

    def comer(self):
        self.comendo = True
        if not self.falar:
            print(f'{self.nome} está comendo')
        else:
            print(f'{self.nome} não pode comer pois está falando.')




if __name__ == '__main__':
    test = Pessoa('Teste', 1)
    test.apresentar()