from socio import Socio, listar_socios
from dependente import Dependente
from salvar_dados import *


def menu():
    print('================= MENU =================')
    print('[1] - Registrar Sócio\n'
          '[2] - Consultar Sócio\n'
          '[3] - Listar Sócios\n'
          '[4] - Registrar Dependente\n'
          '[5] - Consultar Mensalidade\n'
          '[6] - Quitar Mensalidade\n'
          '[7] - Sair')
    option = int(input('Digite a opção desejada: '))
    print()
    return option


def main():
    carregar()
    while True:
        option = menu()
        match option:
            case 1:
                socio = Socio()  # cria o objeto socio
                socio.regSocio()  # entra na função regSocio do objeto e registra as informações no objeto
                set_banco(str(socio.cartao_socio), socio)
                save_info()
                # salva o objeto no dicionário passando o id em string como chave (porque em json as chaves são sempre
                # transformadas em string
            case 2:
                socio = Socio().consSocio()
                # a variável sócio recebe somente a string da função consSocio da classe Sócio (não é um objeto).
                print(socio)  # aqui eu printo as informações retornadas
                print()
            case 3:
                listar_socios()
            case 4:
                id = int(input('Digite o cartão do sócio para ser seu dependente: '))
                banco_de_dados = get_banco()
                if len(banco_de_dados) > 0:
                    registered = False
                    for socio in banco_de_dados.values():
                        if id == socio.cartao_socio:  # se eu encontrar o id (que é o cartão do sócio) no banco de dados
                            registered = True
                            dependente = Dependente()  # crio um objeto
                            quant_dependentes = 0
                            for dependente in socio.dependentes:
                                quant_dependentes += 1
                            # acesso a função do objeto e salvo os dados no objeto
                            info = dependente.regDep(id, quant_dependentes)
                            set_dependente(str(id), dependente)
                            save_info()
                            # salvo o objeto na lista de dependentes do sócio que eu encontrei
                            print(f'Dependente {dependente.nome_dep} registrado com sucesso!\n'
                                  f'Vinculado ao sócio {banco_de_dados[str(id)].nome_socio}.\n')
                            print(f'Seu cartão é: {info}')
                    if not registered:
                        print('Sócio não identificado.\n')  # se printar é porque não achou ninguém com o id passado
                else:
                    print('Ainda não existe nenhum sócio cadastrado.')
            case 5:
                banco_de_dados = get_banco()
                id = int(input('Digite o cartão do sócio para consultar sua mensalidade: '))
                for socio in banco_de_dados.values():
                    if id == socio.cartao_socio:
                        info = socio.mensalidade.consMens()
                        print(info)
            case 6:
                banco_de_dados = get_banco()
                id = int(input('Digite o cartão do sócio para quitar sua mensalidade: '))
                for socio in banco_de_dados.values():
                    if id == socio.cartao_socio:
                        socio.mensalidade.quitarMens()
                save_info()
            case 7:
                print(f'Finalizando.')
                break
            case _:
                print(f'Opção incorreta. Tente novamente\n')


main()
