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


class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self):
        print('Malabarista está apresentando.')


class Palhaco:
    def apresentar_show(self):
        print('Palhaço está apresentando.')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
circo.apresentar(malabarista)
