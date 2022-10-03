from datetime import date


class Pessoa:
    def __init__(self, name, age, talking=False, eating=False):
        self.name = name
        self.age = age
        self.talking = talking
        self.eating = eating

    def __str__(self):
        return self.name

    def talk(self, about):
        if self.eating:
            print(f"{self.name} can't speak while eating.")
            return
        print(f'{self.name} is talking about {about}.')
        self.talking = True

    def eat(self, food):
        if self.talking:
            print(f"{self.name} can't eat while speaking.")
            return
        print(f'{self.name} is eating {food}.')
        self.eating = True

    def get_birth_year(self):
        birth_year = date.today().year - self.age
        return birth_year

