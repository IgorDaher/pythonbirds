class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome=nome
    def cumprimentar (self):
        return 'Hello World'

if __name__ == '__main__':
    p=Pessoa('Gabriel')
    print(p.cumprimentar())
    print(p.nome)
    p.nome='Igor'
    print(p.nome)
    print(p.idade)