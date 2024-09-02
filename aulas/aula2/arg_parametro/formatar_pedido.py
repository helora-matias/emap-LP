def formatar_pedido(item, quantidade = 1, preco_por_unidade = 0):
    total = quantidade * preco_por_unidade
    print(f'Pedido: {quantidade} x {item} a R${preco_por_unidade} cada. Total = R${total}')