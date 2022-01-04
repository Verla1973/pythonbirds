class Pessoa:
    def __init__(self, nome = None, idade = 48):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá!!!{id(self)}'

if __name__ == '__main__':
    p = Pessoa('Verlã')
    print(id(p))
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(f'{p.nome}, {p.cumprimentar()}')
    p.nome = 'Eskurinho Dev'
    print(p.nome)
    print(p.idade)
    print(id(p.idade))
