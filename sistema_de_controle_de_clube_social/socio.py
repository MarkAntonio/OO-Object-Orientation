from categoria import Categoria
from mensalidade import date, Mensalidade
from random import randint
from salvar_dados import get_banco

class Socio:
    def __init__(self) -> None:
        self.cartao_socio = None
        self.nome_socio = None
        self.end_socio = None
        self.tel_socio = None
        self.email_socio = None
        self.categoria = None
        self.dependentes = []
        self.mensalidade = None

    # ========================================= FUNÇÃO SOMENTE PARA TESTES =============================================
    def regSocio(self) -> None:
        print('=========== Criação do Usuário =============')
        self.cartao_socio = self._geradorDeCartao()
        self.nome_socio = str(input('Digite o nome do Sócio: '))
        self.end_socio = str(input('Digite o endereço do Sócio: '))
        self.tel_socio = str(input('Digite o telefone do Sócio: '))
        self.email_socio = str(input('Digite o e-mail do Sócio: '))

        while True:
            print(f'======== Escolha sua Categoria ============\n'
                  f'[1] - Padrão\n'
                  f'[2] - Medium\n'
                  f'[3] - Premium\n'
                  f'[4] - Master')
            op_categoria = int(input('Digite a opção desejada: ')) - 1
            if 3 >= op_categoria >= 0:
                break
            else:
                print('Opção incorreta. Tente novamente.')
        # eu subtraí 1 para que fique compatível com o index da lista das categorias
        self.categoria = Categoria().des_cat[op_categoria]
        # aqui ele recebe umas das categorias da lista de categorias (não é instanciado o objeto)

        print('=========== Mensalidade =============')
        day = int(input('Digite o dia da mensalidade: '))
        month = int(input('Digite o mês: '))
        year = int(input('Digite o ano: '))
        data_mens = date(year, month, day)  # data no tipo "date" (dia - mês - ano)
        if op_categoria == 0:
            valor_mens = 100
        elif op_categoria == 1:
            valor_mens = 200
        elif op_categoria == 2:
            valor_mens = 300
        elif op_categoria == 3:
            valor_mens = 400
        self.mensalidade = Mensalidade(data_mens, valor_mens)

        print('=========== Cadastro Concluido =============')
        print(f'Caro, {self.nome_socio}.\n'
              f'Seu número do cartão de sócio é: {self.cartao_socio}')
        # só coloquei os valores data de mensalidade e valor da mensalidade, os outros serão definidos no momento
        # do pagamento

    def _geradorDeCartao(self):
        banco_de_dados = get_banco()
        cartao = randint(00, 99)
        id = cartao
        if len(banco_de_dados) == 0:
            return cartao
        else:
            info, id = self._consSocio(id, banco_de_dados)
            verificador = id
            if not verificador:
                return cartao
            else:
                return self._geradorDeCartao()

    def consSocio(self) -> str:
        banco_de_dados = get_banco()
        if len(banco_de_dados) == 0:
            return 'Ainda não existe nenhum sócio cadastrado'
        else:
            print('=========== Dados do Sócio =============')
            id = int(input('Digite o cartão do Socio que você deseja consultar: '))
            info, id = self._consSocio(id, banco_de_dados)
            return info

    def _consSocio(self, id, banco_de_dados):
        for socio in banco_de_dados.values():
            if id == socio.cartao_socio:
                id = True
                info = (f'Cartão de Sócio: {socio.cartao_socio}\n'
                        f'Nome: {socio.nome_socio}\n'
                        f'Endereço: {socio.end_socio}\n'
                        f'Telefone: {socio.tel_socio}\n'
                        f'E-mail: {socio.email_socio}\n'
                        f'Categoria: {socio.categoria}')
                if len(socio.dependentes) > 0:  # aqui é só para ficar bonitinho na hora do print.
                    info += '\nDependente(s): '  # ele vai somar as informações na variável "info" e retornar
                    for index, dep in enumerate(socio.dependentes):
                        if index == 0:
                            info += f'{dep.nome_dep}'
                        else:
                            info += f', {dep.nome_dep}'
                else:
                    info += '\nDependente(s): Nenhum'
                return info, id  # eu poderia já printar, mas como o professor disse pra retonar uma string, então estou
        #                     # retornando a "info"
        id = False
        return 'Sócio não identificado.', id  # se cair aqui é porque ele não encontrou o id no banco de dados# #

    #   for socio in banco_de_dados.values():
    #         if id == socio.cartao_socio:
    #             return self._geradorDeCartao()
    #     return cartao


def listar_socios():
    banco_de_dados = get_banco()
    if len(banco_de_dados) > 0:
        print(f'{"ID": <6}{"Nome"}')
        print('=' * 20)
        for socio in banco_de_dados.values():
            print(f'{socio.cartao_socio: <6}{socio.nome_socio}')
        print('=' * 20)
        print()
    else:
        print('Ainda não existem sócios cadastrados')