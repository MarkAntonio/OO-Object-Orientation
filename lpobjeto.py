class Controle:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca


controle = Controle('preta', 'samsung')

setattr(controle, 'marca', "lg")
print(controle.marca)
getattr(controle, 'cor')
