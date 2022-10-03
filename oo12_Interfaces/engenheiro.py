from oo12_Interfaces.interfaces.formas import FormasInterface
from oo12_Interfaces.terrenos.quadrado import TerrenoQuadrado

class Engenheiro:
    def __init__(self, nome) -> None:
        self.nome = nome

    # Não importa qual seja o terreno, desde que esteja de acordo com a implementação de FormasInterface
    def medir_perimetro(self, terreno: FormasInterface):
        if isinstance(terreno, FormasInterface):
            perimetro = terreno.get_perimetro()
            print(f'{self.nome} mediu o perímetro: {perimetro}m.')
        else:
            raise TypeError

    def medir_area(self, terreno: FormasInterface):
        if isinstance(terreno, FormasInterface):
            area = terreno.get_area()
            print(f'{self.nome} mediu o perímetro: {area}m.')
        else:
            raise TypeError
