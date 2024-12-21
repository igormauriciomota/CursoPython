'''
(I) Map, (II) Filter (III) Reduce

(I) Map

A função map() do Python é uma ferramenta que aplica uma função a cada item de uma sequência, 
como uma lista ou dicionário, e retorna um novo iterador com os resultados. 
A função map() é uma opção útil quando se trabalha com múltiplas listas e pode ser mais 
eficiente do que usar um loop for. Ela traz vantagens como: Tornar o código mais conciso, 
Melhorar a legibilidade e entendimento do código, Evitar a necessidade de loops explícitos. 

A sintaxe para a função map() é: map(function, iterable, [iterable 2, iterable 3, ...]). 

A função map() pode ser utilizada com uma função lambda, com uma função definida pelo usuário, 
ou com uma função embutida usando vários argumentos iteráveis. 

def maiorq10(num):
    if num > 10:
        print('Maior')
    else:
        print('Menor')
        
#maiorq10(27)

numero = [4, 6, 5, 91, 12, 8, 7, 14, 15, 16, 17, 18, 3, 2, 1]

result = map(maiorq10, numero)
print(numero)
print(result)
print(type(result))

print(list(result))

# Map com lambda

nascimento = lambda dado: f'Ano de nascimento: {dado[0] - dado[1]}'

dados = [(1998, 22), (1815, 88), (2027, 3)]

print(list(map(nascimento, dados)))

(II) Filter: Filtrar dados

A função filter() do Python é uma ferramenta que permite filtrar elementos de uma sequência com base em 
uma condição específica: 

A sintaxe básica é filter(function, iterable)

O primeiro argumento é uma função que decide se deve incluir ou filtrar cada item
A função é chamada para cada item do iterável passado como segundo argumento
Se a função retornar False, o valor é abandonado

A função filter() tem as seguintes vantagens: 

Melhora a legibilidade do código
É eficiente em termos de tempo de execução e uso de memória
Promove práticas de programação funcional

Para usar a função filter(), pode-se: 

Passar uma função normal
Usar funções lambda, especialmente quando a expressão for menos complexa
Filtrar uma lista de nomes de criaturas de aquário que começam com uma vogal
Filtrar uma lista de objetos
Remover todos os números negativos de uma lista

import math

numeros = [1, 4, 1, 3, 5, 6, 3, 2, 9, 7, 4, 6, 9]
result = filter(lambda num: num > math.pi, numeros) # filter() filtra salva todos os verdadeiros maiores que pi

print(result)
print(type(result))

print(list(result))


<filter object at 0x0000020CA143B9A0>
<class 'filter'>        
[4, 5, 6, 9, 7, 4, 6, 9]

# o que acontece Dentro da função lambda

def qualquer(*args):
    for num in args:
        if num > math.pi: # num e maior que pi
            return True # Verdadeiro
        else:
            return False # Falso
            
            
# filter com map

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# POR PARTES:
# 1 parte: filter(lambda num: num % 2 == 0, numeros) # salvar vaores que saao pares

# 2 parte: map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros)) # Depois eleva estes valores ao quadrado

result = list(map(lambda n: n ** 2, filter(lambda num: num % 2 == 0, numeros)))
print(result)


[4, 16, 36, 64, 100]

(III) Reduce: Relaciona dados posteriores de uma coleção com o resultado da relação de dados anteriores

A função reduce() em Python reduz um iterável, como uma lista, a um único valor. A função aplica 
uma função de dois parâmetros a cada item de uma sequência de entrada, da esquerda para a direita, 
até reduzir o cálculo a um único valor. 

A sintaxe da função reduce() é simples: reduce(função, lista, opcional). O valor opcional é um valor que, 
caso a lista seja nula, é tido como valor padrão

Obs.: Apartir do python3 a função reduce () não e mais integrada (built-in), agora temos
que importar e utilizar essa função a partir do modulo 'functools'

# Exemplo
from functools import reduce

numeros = [2, 1, 2, 3]

result = reduce(lambda x, y: x ** y, numeros)

print(result)

'''

# Exemplo
from functools import reduce

numeros = [2, 1, 2, 3]

result = reduce(lambda x, y: x ** y, numeros)

print(result)

