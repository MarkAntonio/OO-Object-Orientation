from produto import Produto
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
geladeira = Produto('Geladeira', 3459)
fogao = Produto('Fogão', 2199)

car.adicionar_produto(geladeira)
car.adicionar_produto(fogao)
car.finalizar_compra()

car.finalizar_compra()
 
ps5 = Produto('PlayStation 5', 4399)
car.adicionar_produto(ps5)
car.finalizar_compra()
