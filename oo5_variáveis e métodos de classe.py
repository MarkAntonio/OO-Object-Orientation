class Padaria:
    pao_do_dia = 'pão carteira'  #variável de classe (não é recomendado fazer assim)

    def __init__(self, nome_padaria: str) -> None:
        self.nome = nome_padaria

    def print_estatico(self):
        print(self.pao_do_dia)  # na hora de imprimir uma variável de clase declarada fora do init, eu tenho que usar
        # o self mesmo assim

    def mudar_estatico(self):
        self.pao_do_dia = 'Pão de Queijo'

vilabela = Padaria('Vila Bela')


Padaria.mudar_estatico(vilabela)
vilabela.print_estatico()
'''


vilabela.pao_do_dia = 'Pão Francês'  - quando eu mudo uma variável de classe em um objeto, ele muda somente para o obj

Padaria.pao_do_dia = 'Pão Doce' - quando eu mudo uma variável de classe na classe, eu mudo para todos, tanto
para a classe, quanto para os objetos instanciados antes depois da mudança.
porém se eu ja tiver mudado essa variável de classe em um objeto, a mudança que eu fiz na classe não irá valer.

paonosso.pao_do_dia += ' de Côco'
print(vilabela.pao_do_dia)
print(paonosso.pao_do_dia)
print(Padaria.pao_do_dia)
'''


class Restaurante:
    especial = 'Mugunzá com Hiran'  # método da classe

    def __init__(self, nome) -> None:
        self.nome = nome

    def print_especial(self) -> None:
        print(self.especial)

    @classmethod
    def mudar_especial(cls) -> None:  # esse método muda a varíavel da classe, mas não caso a do objeto já foi mudada
        cls.especial = "Feijoada com Coca"



bode_assado_sarapo = Restaurante('Bode Assado Sarapó')
print(bode_assado_sarapo.especial)

bode_assado_sarapo.mudar_especial()
print('Classe', Restaurante.especial)
print('objeto', bode_assado_sarapo.especial)

bode_assado_sarapo.especial = "Bode assado com feijão tropeiro e cajuína"
print(bode_assado_sarapo.especial)

bode_assado_sarapo.mudar_especial()
print(bode_assado_sarapo.especial)


class Loja:

    tarifa = 1.1

    def __init__(self, nome: str, endereco:str) -> None:
        self.nome = nome
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)

    @classmethod
    def vender(cls) -> float:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: float) -> None:
        cls.tarifa = nova_tarifa


alle_store = Loja('Alle Store', 'Avenida Agamenon magalhães')
belababy = Loja('Bela Baby', 'Avenida Presidente Castello branco')

alle_store.apresentar_endereco()
belababy.apresentar_endereco()

print(alle_store.vender())
print(belababy.vender())

belababy.alterar_tarifa(1.4)


print(alle_store.vender())
print(belababy.vender())
