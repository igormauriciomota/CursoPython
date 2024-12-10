"""
1 - Criar um sistema de comando de uma loja de jogos. o programa deve conter pelo menos 6 listas: 
uma indicando quais jogos estão dispoliveis para venda, uma para mostrar o preço de cada jogo, uma para
mostrar a quantidade de jogos disponiveis na loja para venda, uma informando o preço de fabrica 
dos jogos para aumentar o estoque, uma para registrar as vendas e uma para registrar as compras de estoque. 
Todas as informaçoes de um jogo devem estar no mesmo indice nas listas. Criar um menu interativo 
com as seguintes opçoes para o usuario: Registrar venda, Compra de estoque, Resumo da loja, sair.
Ao sair indicar que o caixa esta fechado. O usuario deve controlar o sistema da loja, registrando 
as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade.  

"""
jogos = ['Gow', 'Minecraft', 'GTA', 'Sonic', 'FIFA'] # Jogo disponiveis para venda
precosVenda = [210.00, 2.99, 150.00, 1.80, 125.00] # Preço de venda
precosCompraEstoque = [105.00, 1.50, 75.00, 0.90, 62.50] # Preços para o dono da loja comprar da fabrica
quantidade = [3, 0, 2, 5, 1] # Quantidade de jogos disponiveis
vendas = [] # Vendas registradas
compraDeEstoque = []

op = 0

# SAIR 
while op != 4:
    print('1 - registrar vendas\n2 - Compra de estoque\n3 - Resumo da loja\n4 - Sair')
    op = int(input('Opção: '))
    
    # REGISTRAR VENDAS
    if op == 1:
        jogoVendido = input('Jogo Vendido: ')
        quantidadeVendida = int(input('Quantidade vendida: '))
        if quantidadeVendida <= quantidade[jogos.index(jogoVendido)]: # Testa se a quantidade que o
            print(f'\n{jogoVendido} vendido!')
            quantidade[jogos.index(jogoVendido)] -= quantidadeVendida # Remove do estoque a quantidade vendida
            
            vendas.append(precosVenda[jogos.index(jogoVendido)] * quantidadeVendida) # Adiciona na lista
    # vendas o valor do jogo vendido, encontrado em precosVenda[jogos.index(jogoVendido)]
        else:
            print('\nNão há essa quantidade disponivel em estoque!\n') # caso nao houver a quantidade disponivel
            
    # COMPRA DE ESTOQUE
    elif op == 2:
        jogoComprado = input('Jogo comprado: ')
        quantidadeComprada = int(input('Quntidade comprada: '))
        print(f'{jogoComprado} comprado!')
        quantidade[jogos.index(jogoComprado)] += quantidadeComprada # Adiciona ao estoque a quantidade comprada na fabrica
        compraDeEstoque.append(precosCompraEstoque[jogos.index(jogoComprado)] * quantidadeComprada)
        # Adiciona na lista o valor do jogo comprado
        
    # RESUMO DA LOJA
    elif op == 3:
        print('\n\nQuantidade de jogos em estoque:')
        for jogo in jogos:
            print(f'{jogo}: {quantidade[jogos.index(jogo)]}') # Apresenta a lista de jogos e a quantidade disponivel
        
        print(f'Lucros: R${sum(vendas)}') # soma dos valores da lista 'vendas'
        print(f'Despesas: R${sum(compraDeEstoque)}') # soma dos valores da lista compraDeEstoque
        print(f'Caixa: R${sum(vendas) - sum(compraDeEstoque)}\n') # Determina a receita total da loja pela 
        # subtração dos lucros pelas despesas
        
print('\n\nCaixa Fechado')
