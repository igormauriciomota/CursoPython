'''
Exercícios:

1 - Utilize o módulo random e suas funções para realizar os seguintes procedimentos da tabela abaixo:

----------------------------------------------------------------------------------------------------------------------
| nº | Função           | Procedimentos                                                                               |
|    |                  |                                                                                             |
----------------------------------------------------------------------------------------------------------------------
| 1  | random()         | Obter um número aleatorio inteiro entre 1 e 10 e armazenar em uma variavel X                |
| 2  | Randint()        | Obter X números aleatorios inteiros entre 0 e 100 e armazena-los em uma lista               |
| 3  | shuffle()        | Embaralhar a lista                                                                          |
| 4  | Choice()         | Selecionar um elemento aleatorio da lista                                                   |
| 5  | loop             | Imprimir os números da lista que são maiores que o número selecionado                       |
|_____________________________________________________________________________________________________________________|

1º random() 

# Importando varias funçoes do modulo random
from random import choice as ch
from random import randint as ri
from random import random as rd
from random import shuffle as sh

x = round(rd() * 10) # Número aleatorio multiplicado por 10 e arredondado
print(x) # 

2º Randint() 

# Importando varias funçoes do modulo random
from random import choice as ch
from random import randint as ri
from random import random as rd
from random import shuffle as sh

listaAle = []
x = round(rd() * 10) # Número aleatorio multiplicado por 10 e arredondado
print(x) # 

# for
for i in range(x):
    listaAle.append(ri(0, 100))
    
# O preenchimento poderia ser feito utilizando comprehension
# listaAle = [ri(0, 100) for i in range(x)]

print(listaAle)

3º  shuffle() Embaralha a lista

# Importando varias funçoes do modulo random
from random import choice as ch
from random import randint as ri
from random import random as rd
from random import shuffle as sh

listaAle = []
x = round(rd() * 10) # Número aleatorio multiplicado por 10 e arredondado
print(x) # 
# for
for i in range(x):
    listaAle.append(ri(0, 100))
    
# O preenchimento poderia ser feito utilizando comprehension
# listaAle = [ri(0, 100) for i in range(x)]

print(listaAle)

sh(listaAle) # Embaralha a lista
print(listaAle)

4º Choice()

# Importando varias funçoes do modulo random
from random import choice as ch
from random import randint as ri
from random import random as rd
from random import shuffle as sh

listaAle = []
x = round(rd() * 10) # Número aleatorio multiplicado por 10 e arredondado
print(x) # 
# for
for i in range(x):
    listaAle.append(ri(0, 100))
    
# O preenchimento poderia ser feito utilizando comprehension
# listaAle = [ri(0, 100) for i in range(x)]

print(listaAle)

sh(listaAle) # Embaralha a lista
print(listaAle)

escolhido = ch(listaAle) # Escolhe um elemento aleatorio da lista
print(f'Numero Escolhido: {escolhido}')

5° Loop

# Importando varias funçoes do modulo random
from random import choice as ch
from random import randint as ri
from random import random as rd
from random import shuffle as sh

listaAle = []
x = round(rd() * 10) # Número aleatorio multiplicado por 10 e arredondado
print(x) # 
# for
for i in range(x):
    listaAle.append(ri(0, 100))
    
# O preenchimento poderia ser feito utilizando comprehension
# listaAle = [ri(0, 100) for i in range(x)]

print(listaAle)

sh(listaAle) # Embaralha a lista
print(listaAle)

escolhido = ch(listaAle) # Escolhe um elemento aleatorio da lista
print(f'Numero Escolhido: {escolhido}')

print('Numeros maiores que o escolhido: ', end=' ')
# Loop for
for i in listaAle:
    if i > escolhido:
        print(i, end=' ')
        
# Pode tambem usar o filter
maiores = filter(lambda x: x > escolhido, listaAle)
print(list(maiores), end=' ')

'''
# 1

# Importando varias funçoes do modulo random
from random import choice as ch
from random import randint as ri
from random import random as rd
from random import shuffle as sh

listaAle = []
x = round(rd() * 10) # Número aleatorio multiplicado por 10 e arredondado
print(x) # 
# for
for i in range(x):
    listaAle.append(ri(0, 100))
    
# O preenchimento poderia ser feito utilizando comprehension
# listaAle = [ri(0, 100) for i in range(x)]

print(listaAle)

sh(listaAle) # Embaralha a lista
print(listaAle)

escolhido = ch(listaAle) # Escolhe um elemento aleatorio da lista
print(f'Numero Escolhido: {escolhido}')

print('Numeros maiores que o escolhido: ', end=' ')
# Loop for
for i in listaAle:
    if i > escolhido:
        print(i, end=' ')
        
# Pode tambem usar o filter
# maiores = filter(lambda x: x > escolhido, listaAle)
# print(list(maiores), end=' ')

