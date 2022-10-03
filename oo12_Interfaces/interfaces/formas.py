from abc import ABC, abstractmethod

'''as interfaces acabam sendo representantes das classes em si

Python não tem necessariamente um elemento que seja uma interfaces (em oo).
mas existe uma forma de simular um elemento e apropriar disso como se de fato fossem interfaces. '''

class FormasInterface(ABC):
    @abstractmethod
    def get_perimetro(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_area(self) -> int:
        pass

