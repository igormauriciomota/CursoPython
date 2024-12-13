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
c)  Não ha o efeito Shallow copy, porem a sintax e a mesma (tuplas são sempre independentes)

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
tupla5 = ('futbol', 'moto', 'França')
tupla6 = ('pizza', True, 18, 5j, 0.43, 'x', False)
tupla7 = tuple(range(11))
tupla8 = tuple(['azul', True, 'x', 10, 12.1, 'correio', [1, 2, 3], (1, 2, 3)])

print(type(tupla1), type(tupla2), type(tupla3), type(tupla4))

result: <class 'tuple'> <class 'tuple'> <class 'tuple'> <class 'tuple'>

# concatenação/ a primeira tupla e apagada, e assim foi criada uma nova no momento da concatenação;

tuplaNova = tupla1 + tupla5
print(tuplaNova)

tupla1 = tupla1 + tupla5
print(tupla1)

tupla9 = tupla1 + tupla6
print(tupla9)

result.:
(1, 2, 3, 4, 5, 'futbol', 'moto', 'França')
(1, 2, 3, 4, 5, 'futbol', 'moto', 'França')
(1, 2, 3, 4, 5, 'futbol', 'moto', 'França', 'pizza', True, 18, 5j, 0.43, 'x', False)

# Verificar se determinado valor está em uma tupla

print(10 in tupla8)
print(False in tupla8)
print(True in tupla6)

# Obter a quantidade de vezes que um valor se repete em uma tupla
cores = ('branco', 'azul', 'amarelo', 'verde', 'vermelho', 'roxo', 'lilaz', 'preto', 'verde')

print(cores.count('azul'))
print(cores.count('verde'))

# Acessar elementos de uma tupla/tuplas tambem sao ordenadas
print(tupla8[-3])
print(tupla2[3])
print(tupla6[4])

# Acessar elementos de uma tupla/tuplas tambem sao ordenadas
print(tupla8)
print(tupla8[2])
print(tupla8[4])
print(tupla8[-2])
print(tupla8[-4])

# tupla com for
for indice in range(0, 3):
    print(tupla7[indice])
    
for indice in range(0, 3):
    print(tupla6[indice])
    
# Slicing
print(tupla6)
print(tupla6[2:]) # indice 2 ao final
print(tupla6[2:6]) # indice 2 ao 6
print(tupla6[2:7:2]) # indice 2 ao 7, de dois em dois

# Percorer tuplas (iterar)
# for

for elemento in tupla1:
    print(elemento, end=' ')

total = 0
for elemento in tupla1:
    total = total + elemento
print(f'\nMedia:{total/len(tupla1)}')

1 2 3 4 5 
Media:3.0

# While

total = 0
cont = 0
while cont < len(tupla1):
    total += tupla1[cont] # total = total + tupla1
    cont += 1 # cont = cont + 1
print(tupla1, end=' ')
print(f'\nTotal: {total}')
print(f'\ndivisor: {cont}')
print(f'\nMedia: {total/cont}')

(1, 2, 3, 4, 5) total = 15/5 Media:3.0

# Obter indice da tupla

cores = ('branco', 'azul', 'amarelo', 'verde', 'vermelho', 'roxo', 'lilaz', 'preto', 'verde')

for indice, cor in enumerate(cores):
    print(f'{indice}: {cor}')
    
cores = ('branco', 'azul', 'amarelo', 'verde', 'vermelho', 'roxo', 'lilaz', 'preto', 'verde')

    
print(cores.index('azul'))
print(cores.index('verde'))
print(cores.index('vermelho'))

# Desempacotar tuplas/tem de ser os valores exatos se nao da erro;

esporte, meioTrans, pais = tupla5
print(esporte)
print(meioTrans)
print(pais)

Erros.:
esporte, meioTrans, pais, mais = tupla5
esporte, meioTrans = tupla5

# Funçoes úteis para trabalhar com tuplas

# Obs.: Apenas para inteiros ou floats
print(tupla1)
print(sum(tupla1)) # retorna a soma dos elementos 15
print(max(tupla1)) # retorna o maior elemento 5
print(min(tupla1)) # retorna o menor elemento 1

# Para qualque tipo de dado
print(len(tupla1)) # ler -quntitades de elementos
print(len(tupla8))

# Copiar uma tupla
# Obs.: Não ha o efeito Shallow copy, porem a sintax e a mesma

tuplaNova = tupla1
print(tuplaNova)

tuplaNova = tuplaNova + tupla5
print(tuplaNova)
print(tupla1)

"""

# Exemplos de declaração de tuplas

tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = 1,
tupla4 = (1,)
tupla5 = ('futbol', 'moto', 'França')
tupla6 = ('pizza', True, 18, 5j, 0.43, 'x', False)
tupla7 = tuple(range(11))
tupla8 = tuple(['azul', True, 'x', 10, 12.1, 'correio', [1, 2, 3], (1, 2, 3)])



