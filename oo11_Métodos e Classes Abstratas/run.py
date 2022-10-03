from abs_class import AbstractClass


class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print('Implementando método abstrato')
#      Se eu não colocar esse método abstrato de mesmo nome que o método abstrato definido na classe abstrata,
#      Não será possível instanciar o objeto filha


filha = Filha()
filha.apresentar_metodo()
filha.metodo("I'm here")
filha.metodo_abstrato()
# Erro - não posso instanciar uma classe abstrata
# abstractClass = AbstractClass()
# abstractClass.metodo('Doing something')
