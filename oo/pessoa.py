class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 48):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá!!!{id(self)}'

if __name__ == '__main__':
    amanda = Pessoa(nome='Amanda')
    fernanda = Pessoa(nome='Fernanda')

    eskurinho = Pessoa(amanda, fernanda, nome='Eskurinho')
    print(Pessoa.cumprimentar(self=eskurinho))
    print(eskurinho.cumprimentar())
    for filho in eskurinho.filhos:
        print(filho.nome)
