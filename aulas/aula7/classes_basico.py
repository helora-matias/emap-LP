class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def descricao(self):
        print(f"Nome: {self.nome}, Preço: {self.preco}")


produto = Produto("Maçã", 1.09)

produto.descricao()

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def total_itens(self):
        qtd_itens = self.itens.__len__()
        print(f"Quantidade de itens: {qtd_itens}")
    
carrinho = CarrinhoDeCompras()

produto1 = Produto("Ovos", 6.2)
produto2 = Produto("Galinha", 10.0)

carrinho.adicionar_produto(produto)
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

carrinho.total_itens()