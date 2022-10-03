from produto import Produto

class CarrinhoDeCompras:
    def __init__(self) ->None:
        self.__produtos = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        if len(self.__produtos) == 0:
            print('Ainda não existe nenhum produto no carrinho.')
        else:
            print('Compras finalizadas!')
            for produto in self.__produtos:
                produto.informacoes_produto()
        self.__produtos.clear()