'''
Módulos Integrados e Módulo Random

- Modulos são arquivos Python que podem ser importados para o arquivo principal, geralmente contendo funções.   
- Modulo Randon: possui funçoes que retornam valores pseudo-aleatorios, porem consideramos aleatorios (import)  

(I) Modulo 1 de importação
import random

-> com "import" podemos importar arquivos ja criados

# Obs.: Neste modulo, TODO o modulo e importado, ou seja, todas 
# as classes, funçoes e atributos ficarão disponiuveis na memoria

# Alem do modulo 'random' existe uma função com o mesmo nome:
# Função random: retorna um numero real aleatorio entre 0 e 1 (exclusivo)
print(random.random())

print(random.()) Ao chamarmos o modulo "random." podemos chamar outras funções dentro do modulo

(II) Modulo 2 de importação

from random import randint

Obs.: neste modulo APENAS a função e importada

# Função Randint: Retorna um numero inteiro aleatorio entre os valores dos parametros estabelecidos
print(randint(1, 60))

# Função uniform: retorna um numero real(flot) aleatorio entre os valores dos parametros
from random import uniform
print(uniform(1, 60))

# Função choice: retorna uma valor aleatorio de um iteravel
from random import choice

premios = ['Playstation 2', 'Peixe', 'Chinelo', 'Lápis']
print(f'Mario Ganhou um {choice(premios)}')

# Função Shuffle: retorna o iteravel com os elementos embaralhados
from random import shuffle

cores = ['Preto', 'azul', 'amarelo', 'verde', 'vermelho', 'cinza', 'branco', 'magenta']
print(cores)
shuffle(cores)
print(cores)

=> Todos os modulos podem ser encontrados em https://docs.python.org/3/py-modindex.html

# Função Statistics: Esse módulo fornece funções para o cálculo de estatísticas 
# matemáticas de dados numéricos (para valores do tipo Real ).
import statistics

numeros = [18, 92, 74, 9, 1, 3.8, 4.51]
media = statistics.mean(numeros)
print(media) # 28.90142857142857

(III) Outros modulos de importação/Utilizando alias (as): Apelido de um modulo ou função

Ex.:
-       nome 'as' apelido
import random as rd

print(rd.random())

# Utilizando *: Importa TODAS as funçoes do modulo
from random import *

print(random())

# Importando uma função utilizando alias/agora apelidando a função: choice de 'ch'
from random import choice as ch

lista = ['Navio', 'Batata', 'Acre']
print(ch(lista))

# Importando multiplas funçoes de um mesmo modulo
from random import randint as ri, shuffle as sh

lista = ['Navio', 'Batata', 'Acre']
sh(lista)
print(lista)
print(ri(1, 11))

# Modulo mais utilizado
from random import(
    choice, 
    randint, 
    random, 
    shuffle, 
    uniform
)

print(random())
print(randint(1, 11))
print(uniform(1, 11))
print(choice('Programando Ideias'))
nomes = ['Rebeca', 'Roberta', 'Rubia']
shuffle(nomes)
print(nomes)

'''
# Modulo mais utilizado
from random import choice, randint, random, shuffle, uniform

print(random())
print(randint(1, 11))
print(uniform(1, 11))
print(choice('Programando Ideias'))
nomes = ['Rebeca', 'Roberta', 'Rubia']
shuffle(nomes)
print(nomes)

