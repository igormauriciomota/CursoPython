'''
Dicionarios

a) São apresentados po {}
b) Possuem uma relação chave-> elemento
c) Dicionarios permitem qualquer tipo de dado (int, float, string,....)
d) Não são ordenados
e) São utilizados para otimizar a busca de dados, pois basta voce saber a chave que ira acessar o elemento;

(I) Como declarar?

1-forma (Mais usada):

time_futebol = {'RJ': 'Flamengo', 'SP': 'Corintias', 'MG': 'Cruzeiro'}
print(time_futebol)
print(type(time_futebol))

{'RJ': 'Flamengo', 'SP': 'Corintias', 'MG': 'Cruzeiro'}
<class 'dict'>

2-forma (Utilizando o comando dict()):

times_futebol = dict(RJ='Flamengo', SP='Corintias', MG='Cruzeiro')
print(times_futebol)

3-forma (Menos usada): fronkeys()
# Cria um dicion em cada item dentro do iteravel com o mesmo elemento
# chave = key /Dado = value
nome = {}.fromkeys(iteravel, elemento)
Ex.:
times_futebol = {}.fromkeys('[1234]', 'value')
print(times_futebol)

(II) - Sobre as chaves:

{'chave':}

a) Devem ser únicas
b) podem ser de qualquer tipos
c) Não podem ser repetidas

(III) - Sobre os dados

{'chave': 'dados'}

a) Podem ser duplicados.
b) Podem ser de qualquer tipo
c) Pode ser repetidas

(IV) Formas de acessar o elemento

1 Forma:

times_futebol = {'RJ': 'Flamengo', 'MG': 'Cruzeiro', 'SP': 'Corintias', 'BA': 'Bahia'}
print(times_futebol['RJ'])
aso a chave nao exista ela retorna (erro)

2 Forma:

times_futebol = {'RJ': 'Flamengo', 'MG': 'Cruzeiro', 'SP': 'Corintias', 'BA': 'Bahia'}
print(times_futebol.get('RJ')) # Pegue dentro de times_futebol o elemento dentro da chave 'RJ'
.get() - caso a chave nao exista ela retorna (none)

# Pode perguntar? RJ esta em times_futebol? [in] dentro de
print('RJ' in times_futebol)

O que e None?
- È um tipo de dado sem tipo;
- Usado para declarar variáveis que voce ainda não sabe o tipo que ira utilizar

(V) Adicionar/alterar elementos dentro do dicionario;

1 forma: (Mais otimizada):

sagas = {
    (1,2): 'HP',
    (3,4): 'PJ',
    (5,6): 'JV'
}
print(sagas)
sagas[(7,8)] = 'MR'
sagas[(1,2)] = 'Digimon'
print(sagas)

{(1, 2): 'HP', (3, 4): 'PJ', (5, 6): 'JV'}
{(1, 2): 'Digimon', (3, 4): 'PJ', (5, 6): 'JV', (7, 8): 'MR'}

2 forma: (função update()):

sagas = {
    (1,2): 'HP',
    (3,4): 'PJ',
    (5,6): 'JV'
}

# cria um novo dicionario
dado_novo = {(7,8): 'MR', (9,9): 'SR'}
sagas.update(dado_novo)
sagas.update({(1,2): 'Pokemon'})
print(sagas)


{(1, 2): 'Pokemon', (3, 4): 'PJ', (5, 6): 'JV', (7, 8): 'MR', (9, 9): 'SR'}

(VI) Removendo valores do dicionario: 

1 Forma: Função pop()

pokemon = {
    'Agua': 'Squirtle',
    'Fogo': 'Chamander',
    'Grama': 'Bulbassauro'
}

pokemon.pop('Agua')
print(pokemon)

ou dentro de uma variavel

dado = pokemon.pop('Agua')
print(dado)
print(pokemon)

# O método pop() permite retornar o dado dentro da chave podendo utilizar o elemento posteriormente.  

2 Forma: palavra reservada (del)

pokemon = {
    'Agua': 'Squirtle',
    'Fogo': 'Chamander',
    'Grama': 'Bulbassauro'
}

# não pode usar variavel para armazenar vai dar erro ao utilizar
del pokemon ['Agua']

print(pokemon)

'''


