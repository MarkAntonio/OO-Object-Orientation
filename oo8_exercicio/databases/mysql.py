class MysqlDB:
    def __init__(self):
        self.__conexao = 'Mysql'

    def conectar(self) -> str:
        print('Conectando ao banco Mysql...')
        return self.__conexao

    def desconectar(self) -> None:
        print('Desconectando a Mysql...')