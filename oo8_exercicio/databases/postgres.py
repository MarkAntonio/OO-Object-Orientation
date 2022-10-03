class PostgresDB:
    def __init__(self):
        self.__conexao = 'Postgres'

    def conectar(self) -> str:
        print('Conectando ao banco Postgres...')
        return self.__conexao

    def desconectar(self) -> None:
        print('Desconectando a Postgres...')