from typing import Type

'''No diagrama de Classes o atributo de classe é um atributo que tem um risco em baixo.
'''


class Interruptor:


    def __init__(self, comodo: str):
        self.__comodo = comodo

    def acender(self):
        print(f'Acendendo {self.__comodo}...')

    def apagar(self):
        print(f'Apagando {self.__comodo}...')


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        if isinstance(interruptor, Interruptor):
            interruptor.acender()
        else:
            raise Exception('This objet is not a "Interruptor" type.')

    def apagar_luz(self, interruptor: Interruptor):
        interruptor.apagar()

    def dormir(self):
        print('Foi dormir...')

class Fire:
    def __init__(self):
        self.type = 'Fogo'

    def acender(self):
        print(f'Acendendo o {self.type}')


Marco = Pessoa()
interruptor_quarto = Interruptor('Quarto')
interruptor_cozinha = Interruptor('Cozinha')

fire = Fire()

interruptor_quarto.acender()
Marco.acender_luz(interruptor_quarto)
Marco.apagar_luz(interruptor_cozinha)
Marco.dormir()
