
# Essa classe está fechada. Existem casos que podem ser assim, mas o ideal é usar o princípio aberto fechado
class Circo:
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        elif tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista se apresentando.')

    def apresentar_palhaco(self):
        print('Palhaço se apresentando.')


circo = Circo()
circo.apresentar(1)
circo.apresentar(2)


# agora sim está com o princípio aberto fechado
# ela está fechada para alterações, mas está aberta para extensões
# entradas diferentes geram ações diferentes.

class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

# essas classes vão funcionar, desde que eles tenham o método apresentar_show
class Malabarista:
    def apresentar_show(self):
        print('Malabarista está apresentando.')


class Palhaco:
    def apresentar_show(self):
        print('Palhaço está apresentando.')

class Domador:
    def apresentar_show(self):
        print('Domador apresentou seu show.')

circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
circo.apresentar(malabarista)
domador = Domador()
circo.apresentar(domador)
# E o Circo continua funcionando desde que o apresentador, seja ele qual for,
# possua o método esperado para apresentar o show, porque o show não pode parar!
# e daqui vai gerar a herança e interfaces.
