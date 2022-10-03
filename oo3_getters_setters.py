class Pessoa:
    def __init__(self, name: str,  idade: int) -> None:  # retona None
        self.name = name
        self.idade = idade

    def drive(self, veicle) -> None:  # retona None
        print(f'Driving a {veicle}')

    def sing(self) -> None:  # retona None
        print(f'dó ré mi fá sol')

    def get_age(self) -> int:  # retona int
        return self.idade

# ======================================================================================


class Alarm:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor


desperta_jovem = Alarm(True)
print(desperta_jovem.get_estado())
desperta_jovem.set_estado(False)
print(desperta_jovem.get_estado())