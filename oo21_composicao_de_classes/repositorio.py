from sql_actions import Insert, Select

class Repositorio:
    def __init__(self):
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self):
        self.__select.select_one()