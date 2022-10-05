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


class Hand:
    def __init__(self, side):
        self.side = side


class Door:
    def __init__(self, room_name):
        self.room_name = room_name

    def open(self, hand: Hand):
        print(f'Opening {self.room_name} door with my {hand.side} hand.')

    def close(self, hand: Hand):
        print(f'Closing {self.room_name} door with my {hand.side} hand.')


class Person:
    def __init__(self, name):
        self.name = name

    def open_door(self, door: Door, hand: Hand):
        door.open(hand)

    def close_door(self, door: Door, hand: Hand):
        door.close(hand)


right_hand = Hand('right')
left_hand = Hand('Left')
bathroom_door = Door('bathroom')
kitchen_door = Door('kitchen')
heldon = Person('Héldon')
heldon.open_door(bathroom_door, right_hand)
heldon.open_door(kitchen_door, left_hand)
kitchen_door.close(right_hand)