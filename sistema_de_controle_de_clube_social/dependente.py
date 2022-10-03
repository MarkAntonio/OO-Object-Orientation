class Dependente:
    def __init__(self) -> None:
        self.cartao_dep = None
        self.nome_dep = None
        self.parentesco = None
        self.email_dep = None

    def regDep(self, cartao_socio, quant_dep) -> str:
        self.cartao_dep = f'{cartao_socio} - 0{quant_dep + 1}'
        self.nome_dep = str(input('Digite o nome do dependente: '))
        while True:
            print('====== Escolha seu Parentesco =======\n'
                  '[1] - Pai ou mãe\n'
                  '[2] - Tio ou tia\n'
                  '[3] - Primo ou prima\n'
                  '[4] - Sobrinho ou sobrinha\n'
                  '[5] - Outro parentesco/parente distante')
            op = int(input('Digite a opção: '))
            if 5 >= op >= 1:
                break
        match op:
            case 1:
                parentesco = 'Pai/mãe'
            case 2:
                parentesco = 'Tio/tia'
            case 3:
                parentesco = 'Primo/prima'
            case 4:
                parentesco = 'Outro/parente distante'
        self.parentesco = parentesco
        self.email_dep = str(input('Digite o e-mail do dependente: '))
        return self.cartao_dep  # ele retorna o cartão, mas não faz nada com ele. Só retonei porque o professor pediu
