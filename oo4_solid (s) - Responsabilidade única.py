class SistemaCadastral:

    def cadastar(self, nome: str, idade: int) -> None:
        if self.__verify_data(nome, idade):
            self.__register_info(nome, idade)
        else:
            self.__show_error()

    def __verify_data(self, nome:str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)

    def __register_info(self, nome:str, idade: int) -> None:
        print(f'Cadastrando usuário {nome} de idade {idade}.')
        print(f'Informações registradas no banco de dados com êxito.')

    def __show_error(self) -> None:
        print(f'invalid info.')


sys = SistemaCadastral()
sys.cadastar('Marco', 20)

'''SRP — Princípio da responsabilidade única
Na programação, o Princípio da responsabilidade única declara que cada módulo ou classe deve ter responsabilidade sobre 
uma única parte da funcionalidade fornecida pelo software.

Você pode ter ouvido a citação: “ Faça uma coisa e faça bem “.
Isso se refere ao princípio da responsabilidade única.
No artigo citado acima, Robert C. Martin define uma responsabilidade como um “motivo para mudar” e conclui que uma 
classe ou módulo deve ter um e apenas um motivo para ser alterado.

Como esse princípio nos ajuda a criar um software melhor? Vamos ver alguns dos seus benefícios:

Teste — Uma classe com uma responsabilidade terá muito menos casos de teste
Menor acoplamento — menos funcionalidade em uma única classe terá menos dependências
Organização — Classes menores e bem organizadas são mais fáceis de pesquisar do que as classes monolíticas'''