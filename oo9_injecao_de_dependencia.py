from typing import Type


# Aqui ainda não é uma relação de dependência, mas sim de associação

class House:
    def __init__(self):
        self.__address = 'Rua Rufino Nicolau'

    def turn_on_lights(self):
        print("I'm turning on the lights")

    def get_address(self):
        return self.__address


class Person:
    def __init__(self, name: str):
        self.__name = name

    def entering_the_place(self, place: any):
        place.turn_on_lights()

    def show_place(self, place: any):
        address = place.get_address()
        print(address)


my_sweet_home = House()
girl = Person('Isla')
girl.show_place(my_sweet_home)
girl.entering_the_place(my_sweet_home)

print('Daqui pra baixo sim é dependência.')

class House:
    def __init__(self) -> None:
        self.__address = 'Rua Rufino Nicolau'

    def turn_on_lights(self) -> None:
        print("I'm turning on the lights")

    def get_address(self) -> str:
        return self.__address


class Person:
    def __init__(self, name: str, local: Type[House]) -> None:
        self.__local = local  # é dependência pois para criar o obj é preciso colocar o local no construtor
        self.__name = name

    def entering_the_place(self) -> None:
        self.__local.turn_on_lights()

    def show_place(self) -> None:
        address = self.__local.get_address()
        print(address)


my_sweet_home = House()
girl = Person('Isla', my_sweet_home)
girl.show_place()
girl.entering_the_place()
