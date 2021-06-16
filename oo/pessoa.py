class Pessoa:
    boca=1
    def __init__(self,*filhos, nome=None, idade=35):
        self.idade = idade
        self.nome=nome
        self.filhos=list(filhos)
    def cumprimentar (self):
        return 'Hello'

if __name__ == '__main__':
    gabriel=Pessoa(nome='Gabriel')
    igor = Pessoa(gabriel, nome='Igor')
    #print(Pessoa.cumprimentar(igor))
    print(igor.nome)
    print(igor.idade)
    for filho in igor.filhos:
        print(filho.nome)
    igor.sobrenome='Daher'
    print(igor.sobrenome)
    del igor.filhos
    igor.boca=2
    print(igor.__dict__)
    print(gabriel.__dict__)
    print(Pessoa.boca)
    print(Pessoa.boca,gabriel.boca, igor.boca)
