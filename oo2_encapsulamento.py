class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def beber(self, bebida):
        if bebida == "redbull":
            self.__get_cpf()
        else:
            print('pode tomar sem mostrar o decumento, meu patrão.')
        print(f'tomando um {bebida}zim...')

    def __get_cpf(self):
        print(f'Cpf desse safado é {self.__cpf}')

geraldo = Pessoa('Geraldo', 24, '134.098.456-08')
geraldo.beber('redbull')


class Calculadora:
    def calculate(self, op, num1, num2):
        if op == '+':
            return self.__add(num1, num2)
        elif op == '-':
            return self.__sub(num1, num2)
        else:
            print('invalid operation.')

    def __add(self, num1, num2):
        return num1 + num2

    def __sub(self, num1, num2):
        return num1 - num2


calculadora = Calculadora()
res = calculadora.calculate('g', 1, 2)
print(res)