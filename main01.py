from pessoa01 import Pessoa

p1 = Pessoa('irineu', 37)

print(p1.age)
print(p1.talk('Jesus'))
print(f'{p1.name} nasceu no ano de {p1.get_birth_year()}')
print(p1.eat('sopa'))

