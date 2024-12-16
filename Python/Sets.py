'''
Sets (Conjunto)

Caracteristicas de conjuntos:

1) Não sao ordenados
2) Não aceitam elementos repetidos
3) São representados por chaves {}, porem não possuem a relação chave->dado;

Qual a vantagem de utilizar conjunto?

1) Conjuntos apresentam formas otimizadas de realizar funçoes especificas que só ele possui;
2) Os conjuntos são altamente otimizados para testes de associação, sendo mais eficientes do que as listas. 
3) Os conjuntos removem automaticamente duplicatas. 
4) Os conjuntos suportam operações matemáticas como união, interseção, diferença e diferença simétrica. 

Os conjuntos utilizam uma tabela de dispersão (hash table) para uma busca eficiente de elementos. 
Os conjuntos são coleções não ordenadas de elementos únicos, o que significa que não é possível 
acessar os itens usando índices como nas listas. 

Existe basicamente duas 2 formas de declar;

1 forma (Mais usada):

nome = {dado1,dado2,dado3,...}
Ex:

conjunto = {1,2,3,4,5,6,6,6,6}
print(conjunto)
print(type(conjunto))

# Não aceita elementos repetidos
{1, 2, 3, 4, 5, 6}
<class 'set'>

2 forma Função set()
nome = set(iteravel)

Alguns exemplos de dados iteráveis em Python são: 
Listas, Tuplas, Conjuntos, Dicionários, Strings de caracteres, Objetos arquivo.
Ex:

Lista
conjunto = set([1,2,3,4,5])
print(conjunto)
print(type(conjunto))

Tuplas
conjunto = set((1,2,3,4,5,6,6,6))
print(conjunto)
print(type(conjunto))

Exemplo:

A - conjunto são iteraveis, logo podemos aplicar-los no for:

pares = {2,4,6,8,10,12,14}

for num in pares:
    print(num, end=' ')

B - Metodo in(dentro):

nome = {'Ana', 'Bruno', 'Flavia'}

if 'Ana' in nome:
    print('Tem uma Ana')
    print('Ana' in nome)
else:
    print('Sumiu!')   
    
Tem uma Ana
True
    
    
C - Adicionar elementos dentro do conjunto;

esportes = {'Futbol', 'Volei', 'Peteca', 'Natação'}
esportes.add('Judo')
print(esportes)

{'Peteca', 'Natação', 'Futbol', 'Judo', 'Volei'}

esportes = {'Futbol', 'Volei', 'Peteca', 'Natação'}
esportes.add(input('Adicionar um Esporte: '))
print(esportes)

D - Remover elemento do conjunto:

1 Forma: veriavel.remove()

conjunto = {1,2,3,4,5,6,7,8}
conjunto.remove(8)

retorno = conjunto.remove.(8)
print(conjunto)
print(retorno) # Retorna None

# input()
conjunto = {1,2,3,4,5,6,7,8}
conjunto.remove(int(input('Remova o elemento de 1 a 8: ')))
print(conjunto)

2 Forma: variavel.dscard()

conjunto = {1,2,3,4,5,6,7,8}
conjunto.discard(8)
print(conjunto)

conjunto = {1,2,3,4,5,6,7,8}
conjunto.discard(int(input('Remova o elemento de 1 a 8: ')))
print(conjunto)

3 Forma: pop() Elimina um de cada vez a cada pop()
- Metodo pop nao necessita de mandar elemento, assim ele ira remover um valor arbitrario e desordenado

Ex.1

conjunto = {1,2,3,4,5,6,7,8}
conjunto.pop() 
conjunto.pop()
conjunto.pop()
print(conjunto)

{4, 5, 6, 7, 8}

Ex.2

conjunto = set('Homem de Aço')
conjunto.pop()
print(conjunto)

{'ç', ' ', 'o', 'A', 'e', 'd', 'm'}

4 Forma: clear() Limpa o conjunto, mas nao o apaga;

conjunto = {1,3,5,7,9,11}
conjunto.clear()
print(conjunto)
conjunto.add(1)
conjunto.add(2)
print(conjunto)

set()
{1, 2}

- Função len() Retorna o comprimento do conjunto/ numeros de elementos;

conjunto = {1,2,3,4,5,7,9,11}
print(len(conjunto))

- Intersecção de conjuntos (Valores que possuem em ambos): Intersection()

1-Ex:

nota_fabil = {5,6,7}
nota_Clara = {6,7,8}
# qual o elemento da nota fabil: esta tambem na nota clara!
print(nota_fabil.intersection(nota_Clara))

{6,7}

2-Ex: sem o Intersection()

nota_fabil = {5,6,7}
nota_Clara = {6,7,8}
# qual o elemento da nota fabil: esta tambem na nota clara!
print(nota_fabil & nota_Clara)

- União de conjuntos (Junta todos os valores de um e outro): union()

Ex: 1

nota_fabil = {5,6,7}
nota_Clara = {6,7,8}
# Juntar a nota de fabil e clara!
print(nota_fabil.union(nota_Clara))

{5, 6, 7, 8}

Ex: 2 sem usar o union()

nota_fabil = {5,6,7}
nota_Clara = {6,7,8}
# Juntar a nota de fabil e clara!
print(nota_fabil | nota_Clara)

- Difference() - Elementos que possuem em apenas um deles:

Resposta: {5}
nota_fabil = {5,6,7}
nota_Clara = {6,7,8}
# Juntar a nota de fabil e clara!
print(nota_fabil.difference(nota_Clara))

Resposta: {8}
nota_fabil = {5,6,7}
nota_Clara = {6,7,8}
# Juntar a nota de fabil e clara!
print(nota_Clara.difference(nota_fabil))

-> Deep copy

copy() - Cada conjunto vai trabalhar separadamente;

conjunto = {'vish','deu','ruim','deep','copy'}
conjunto_novo = conjunto.copy()
conjunto_novo.add('onde')
print(conjunto)
print(conjunto_novo)

- Result:
{'deep', 'ruim', 'copy', 'deu', 'vish'}
{'onde', 'deep', 'ruim', 'copy', 'deu', 'vish'}

-> Shallow Copy 

conjunto = {'vish','deu','ruim','deep','copy'}
conjunto_novo = conjunto
conjunto_novo.add('onde')
print(conjunto)
print(conjunto_novo)

- Result
{'vish', 'ruim', 'copy', 'deu', 'deep', 'onde'}
{'vish', 'ruim', 'copy', 'deu', 'deep', 'onde'}

-> Max: Maximo = 88
-> Min: Minimo = 1
-> Sum: Soma = 151

valores = {1,6,2,8,3,7,11,25,88}
print(max(valores))
print(min(valores))
print(sum(valores))

'''

valores = {1,6,2,8,3,7,11,25,88}
print(max(valores))
print(min(valores))
print(sum(valores))
