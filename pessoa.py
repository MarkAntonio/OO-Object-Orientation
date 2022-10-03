from datetime import date, datetime


class Pessoa:
    # ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    ano_atual = date.today().year  # variável da classe. posso usar tanto na classe tanto no objeto.

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # variavel = "valor"  # disponível apenas na função __init__
        # print(variavel)

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:  # se comendo for True
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        # return self.ano_atual - self.idade
        print(self.ano_atual - self.idade)

    @classmethod  # método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa('Pedro', 28)
p2 = Pessoa('Clara', 27)
p3 = Pessoa('Luiz', 1987)
print(p1.idade)
p1.get_ano_nascimento()
p3.get_ano_nascimento()
