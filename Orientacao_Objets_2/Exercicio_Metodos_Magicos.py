'''
1 - Um escritor de livros pretende escrever e lançar edições para atingir a
quantia de 1 milhão de reais. Simplesmente por este motivo, crie uma classe
que receberá em seu método construtor o nome do livro e o número de
páginas. Além disso, também deve ser criado um atributo no construtor para a
edição do livro, que será atualizado em uma unidade a cada livro que for
publicado. Por fim, utilize randint() para gerar um valor entre 0 e 500 mil,
representando a arrecadação das vendas, o último atributo do construtor.
Crie o método mágico __repr__ para representar o nome do livro e a edição.
Ainda, utilize __len__ para determinar o número de páginas de cada livro. Por
fim, verifique se o valor total de arrecadações atingiu 1 milhão de reais.

'''

from random import randint as ri


class Livros:
    # Metodo construtor tambem e um metodo magico
    def __init__(self, nome, numPg, edicao, valorArre):
        self.nome = nome
        self.numPg = numPg
        self.edicao = edicao
        self.valorArre = valorArre
        
    def __repr__(self):
        return f'{self.nome} - Edição {self.edicao}'
    
    def __len__(self):
        return self.numPg
    
    
#Objetos
livro1 = Livros('Harry Poter e as Reliquias da Morte', 551, 1, ri(0, 5000000))
livro2 = Livros('O Pequeno Principe', 96, 2, ri(0, 5000000))
livro3 = Livros('Mar Sem Fim', 308, 3, ri(0, 5000000))
        

print(livro1)
print(livro2)
print(livro3)

print(f'livro 1: {len(livro1)} páginas')
print(f'livro 2: {len(livro2)} páginas')
print(f'livro 3: {len(livro3)} páginas')

print(f'Arrecadação Livro 1: {livro1.valorArre}')
print(f'Arrecadação Livro 2: {livro2.valorArre}')
print(f'Arrecadação Livro 3: {livro3.valorArre}')

valorTotal = livro1.valorArre + livro2.valorArre + livro3.valorArre

if valorTotal > 1000000:
    print('\nParabéns! Voce agora e um milionario!')
else:
    print('\nTende vender mais livros!')
print(f'valor arrecadado: {valorTotal}')



