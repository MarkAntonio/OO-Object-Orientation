from oo12_Interfaces.interfaces.formas import FormasInterface

'''Colocamos como se fosse uma herança, mas quando falamos de interface, é de fato uma implementação'''


class TerrenoQuadrado(FormasInterface):
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def get_perimetro(self) -> int:
        perimetro = self.lado * 4
        return perimetro

    def get_area(self) -> int:
        area = self.lado * self.lado
        return area

