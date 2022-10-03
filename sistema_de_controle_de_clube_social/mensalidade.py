from datetime import date, timedelta


class Mensalidade:
    def __init__(self, data_mens: date, valor_mens: float) -> None:
        self.data_mens = data_mens
        self.valor_mens = valor_mens
        self.data_pgto_mens = None
        self.juros_mens = None
        self.valor_pago = None
        self.quit_mens = False

    def consMens(self) -> str:
        print('======= Consulta de Mensalidade ======')
        valor_str = f'{self.valor_mens:.2f}'
        if not self.quit_mens:
            info = f'Data de pagamento: {self.data_mens.strftime("%d/%m/%y")}\n' \
                   f'Valor da mensalidade: R$ {valor_str.replace(".", ",")}'
            return info
            # retorna a string info com as informações
        else:
            return 'A mensalidade deste mês já foi quitada.\n'

    def cal(self, current_date):
        data_venc = self.data_mens
        var = 0
        while data_venc != current_date:
            data_venc = data_venc + timedelta(1)
            var += 1
        return var

    def quitarMens(self):
        data_venc = self.data_mens
        print('======== Quitar Mensalidade ========')
        day = int(input('Digite o dia: '))
        month = int(input('Digite o mês: '))
        year = int(input('Digite o ano: '))
        data_atual = date(year, month, day)
        dias = self.cal(data_atual)
        if data_venc > data_atual:
            self.quit_mens = False
        if dias <= 30:
            valor = f'{self.valor_mens:.2f}'
            print('Valor da mensalidade R$', valor.replace(".", ","))
            while True:
                print('[1] - Confirmar pagamento')
                print('[2] - Sair')
                op = int(input('Digite a opção: '))
                if op == 1:
                    self.quit_mens = True
                    if data_venc < data_atual:
                        self.data_mens = data_venc + timedelta(30)
                    else:
                        dias2 = dias
                        dias2 = dias2 / 2
                        dias2 = int(dias2)
                        dias2 = dias2 * 30
                        self.data_mens = data_venc + timedelta(dias2)
                    self.valor_pago = self.valor_mens
                    print('Pagamento confirmado')
                    return
                elif op == 2:
                    return
        elif dias > 30:
            valor = self.valor_mens
            if dias > 30:
                mes = dias / 30
                mes = int(mes)
                valor = valor * mes

            valor_juro = valor * (dias * 0.01)
            valor_juro_str = f'{valor_juro:.2f}'
            valor_total = f'{valor + valor_juro:.2f}'
            print("=" * 20)
            print('Mensalidade vencida a', dias - 30, 'dias.')
            print(f'Valor do juros de atraso: R$', valor_juro_str.replace(".", ","))
            print(f'Valor total: R$', valor_total.replace(".", ","))
            print("=" * 20)
            while True:
                print('[1] - Confirmar pagamento')
                print('[2] - Sair')
                op = int(input('Digite a opção: '))
                if op == 1:
                    self.quit_mens = True
                    self.data_mens = data_venc + timedelta(30)
                    print('Pagamento confirmado')
                    return
                elif op == 2:
                    return
    # aqui eu vou pedir que o usuário digite a "data de pagamento" para que eu possa calcular os "juros" caso eles
    # esteja atrasado da data de pagamento que ele digitou com cadastrou o sócio.

    # aí o usuário vai digitar o valor de pagamento. Se ele pagar tudo certo a conta é quitada
    # (self.quit_mens = True) e ele retorna True (só porque o professor mandou, mas não vai usar pra nada)

    # Se não estiver tudo certo, ele não salva as informações e retorna False (só porque o professor mandou)
