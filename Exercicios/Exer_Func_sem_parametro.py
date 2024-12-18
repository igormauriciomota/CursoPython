'''
Exercícios:

1) Foi realizada uma pesquisa de algumas características e gostos de quatro
habitantes incluindo: nome, sexo, esporte favorito (Natação, Futebol, Volêi,
Tênis) e idade. Com esses dados faça:

- Função que armazene os dados em uma lista. Dica: Use dicionários dentro da
lista.

- Calcule a idade média de homens que gostam de natação. Caso não haja
homens que gostam de natação chame uma função e imprima um aviso de que
não há homens que gostam de natação.

'''

def cadastro():
    list = []
    for i in range(4):
        # Criação de um dicionario para cada pessoa, facilitando localizar elementos
        dicionario = dict(nome = input('Digite seu nome: '), sexo =
                          input('Digite M para masculino e F para feminino: '), esporte =
                          input('Escolha seu esporte favorito entre natacao, futebol, volei, tenis: '), idade = 
                          int(input('Digite sua idade: ')))
        list.append(dicionario) # Adiciona o dicionario na lista
    return list # rtorna a lista

# Mensagem de que não existem homens que gostam de natação
def aviso():
    print('Não tem homens que gostam de natação')
    
lista = cadastro()
cont = 0
soma = 0

for i in range(4):
    if lista[i]['sexo'] == 'M' and lista [i]['esporte'] == 'natacao':
        soma = soma + lista[i]['idade'] # Somar a idade de todos os homens que gostam de natação;
        
        cont += 1
if cont == 0: # caso não há homens que gostem de natação faça;
    aviso()
else:
    media = soma / cont # calcula a media
    print(f'A idade media de homens que fazem natação é {media}') # imprime a media de idade

