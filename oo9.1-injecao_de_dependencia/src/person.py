class Person:
    def __init__(self, action):
        self.__behavior = action

    def make_action(self):
        self.__behavior.action()
