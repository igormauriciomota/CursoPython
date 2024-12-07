"""
1 - Crie duas listas, uma para o carrinho do supermercado que ira receber produtos comprados e outra
para os preços dos produtos. Utilizando um loop, preencha as listas com 5 produtos e 5 preços, recebendo
estes dados do usuario (input). Por fim, some os preços, imprima o valor total e os produtos do carrinho.  

"""
# 1 lista
listaCarrinho = [] # Criando a lista que vai receber os produtos
listaPrecos = [] # Criando a lista que vai receber os preços
contProdutos = 0
valorTotal = 0
produto = ''

while contProdutos < 5: # Loop para acrescentar 5 itens nas listas
    produto = input('Produto: ') # Incerir produto
    listaCarrinho.append(produto)
    preco = float(input('Preço: '))
    listaPrecos.append(preco)
    contProdutos += 1
    
for id in range(0, 5): # 0, 1, 2, 3, 4
    valorTotal += listaPrecos[id] # somando todos os elementos da lista

print(f'Produtos comprados: {listaCarrinho}')
print(f'Valor total: R$ {valorTotal}')
