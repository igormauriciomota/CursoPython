from random import choice as ch


def sorteio(cartela1, cartela2, max):
    numSorteados = []
    numerosIniciais1 = []
    numerosIniciais2 = []
    vencedor = ''
    sorteador = list(range(1, max + 1)) # Cria uma lista com numero de 1 até max
    while vencedor == '':
        numS = ch(sorteador) # Escolhe um numero da lista 'Sorteador'
        sorteador.pop(sorteador.index(numS)) # O numero escolhido é depois removido da lista 
# para nao haver repetição dos numeros sorteados
        numSorteados.append(numS)
        if numS in cartela1:
            numerosIniciais1.append(cartela1.pop(cartela1.index(numS))) # Se a cartela (lista) da pessoa dispor do numero
# sorteador, ele é removido dela. Em seguida é adicionado a lista 'numerosIniciais1' para no final todos os numeros dessa 
# lista serem apresentados como os numeros que havia na cartela (lista.)
            if len(cartela1) == 0: # Testa se a pessoa ganhou (não há numeros em sua cartela)
                vencedor = 'João'
                print(f'Vencedor: {vencedor}')
                print(f'Cartela: {numerosIniciais1}')
        if numS in cartela2:
            numerosIniciais2.append(cartela2.pop(cartela2.index(numS)))
            if len(cartela2) == 0: # Testa se a pessoa ganhou (não há numeros em sua cartela)
                vencedor = 'Maria'
                print(f'Vencedor: {vencedor}')
                print(f'Cartela: {numerosIniciais2}')
    print(f'Numeros sorteados: {numSorteados}')        
            
            
            