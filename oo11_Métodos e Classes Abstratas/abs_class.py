from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def __init__(self):
        self.atributo = 'Olá Mundo'

    def metodo(self, elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self):
        pass

'''eu não posso ter instância de uma classe abstrata

Mas Para pyton, para eu ter uma classe abstrata, além de herdar o objeto ABC (abstrato) ele precisa
ter no mínimo uma função abstrata'''