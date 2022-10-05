from src.person import Person
from src.actions.talk import Talk
from src.actions.run import Run


severino = Person(Talk())
neymar = Person(Run())

severino.make_action()

neymar.make_action()
