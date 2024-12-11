"""
Tuplas

Parecem listas, mas possuem duas 2 diferenças: 

1° Diferença: Não é possivel remover ou adicionar elementos, apenas sobrescreve-las.  

2º Diferença: sintax:() parenteses ex.: (elemento1, elemento2, elemento3, ..., elementoN)
o que determina nao são os parentesis mas a virgula "," que separa os elementos
pode ser tambem so separado por virgula e obrigatoia! ex.: elemento1, elemento2, elemento3, ..., elementoN

(I) Vantagens das Tuplas em relação as listas:

a) Dados são mais seguras
b) Processamento e mais rapido
c) Não há shallow copy (tuplas são sempre independentes)

(II) Quando usar?

Usar quando não forem necessarias modificaçoes nos dados.   
Ex.: Calendario -> armasenar - Meses do ano, dias da semana.  

(III) type() - Para determinar o tipo de um objeto em Python, a função type exibe o tipo de uma variável ou valor.

ex.:

# Exemplos de declaração de tuplas

tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1,)

print(type(tupla1), type(tupla2), type(tupla3), type(tupla4))

result: <class 'tuple'> <class 'tuple'> <class 'tuple'> <class 'tuple'>

"""

# Exemplos de declaração de tuplas

tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1,)

print(type(tupla1), type(tupla2), type(tupla3), type(tupla4))
