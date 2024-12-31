'''
Geradores 

- São iteradores, basicamente são objetos que voce pode percorrer como listas 
porem eles nao armazenam na memoria;

- Só podem iterar(loops/funções) apenas uma vez geradores;

- As funçoes que geram geradores são chamadas de funções geradoras;

- Para retornar o conteudo presente em uma função geradora usa-se ao inves da palavra return, palavra reservada yield;

- Sendo que funções geradoras retornam um elemento por vez;

- Geradores trazem performace tanto em memoria quanto em velocidade no codigo, pois só podem ser usados uma vez;


Exemplo 1

def funcao_geradora():
    while True: # Loop infinito
        palavra = input('fale: ')
        yield palavra
        
resultado = funcao_geradora()
print(resultado) # Gera somente um ojeto
# Ele irá gerar loop de acordo com a quantidade de next()
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))

Obs.: Caso use um loop for, cuidado para não cair em um loop infinito:
# Utilize um contador no loop while
def funcao_geradora():
    auxiliar = 0
    while auxiliar < 5: # Loop infinito/ tem de ter uma parada
        auxiliar += 1
        palavra = input('fale: ')
        yield palavra
        
resultado = funcao_geradora()
print(resultado) # Gera somente um ojeto

for item in resultado:
    print(item)


Exemplo 2

def funcao_geradora():
    auxiliar = 0
    while auxiliar < 5: # Loop infinito
        auxiliar += 1
        palavra = input('fale: ')
        yield palavra
        
resultado = funcao_geradora()
print(resultado) # Gera somente um ojeto

# Podemos manipular geradores e transforma-los no que quisermos(set,list,tuple,dict)

# print(list(resultado))  ['1', '2', '3', '4', '5']
print(set(resultado)) # {'5', '1', '9', '6', '3'}
# 1print(tuple(resultado))

Geradores -> Não será executado a proxima iteração pois geradores só pedem ser iterados uma vez

def funcao_geradora():
    auxiliar = 0
    while auxiliar < 5: # Loop infinito
        auxiliar += 1
        palavra = input('fale: ')
        yield palavra
        
resultado = funcao_geradora()
print(resultado) # Gera somente um ojeto

for item in resultado:
    print(resultado)

# Não será executado a proxima iteração pois geradores só pedem ser iterados uma vez
for x in resultado:
    print(x)
    
(I) Teste de velocidade:

# Bibilioteca-> time

import time  # Importando toda bibilioteca

# list comprehension
tinicio_lista = time.time()
print(sum([valor ** 2 for valor in range(100000000)]))
tfinal_lista = time.time() - tinicio_lista

# Generator comprehension
tinicio_gen = time.time()
print(sum((valor ** 2 for valor in range(100000000))))
tfinal_gen = time.time() - tinicio_gen

print(f'Lista levou {tfinal_lista}') #
print(f'Generator levou {tfinal_gen}') #

Tempo de resposta:
Valo: 333333328333333350000000
Lista levou 131.77676367759705  
Generator levou 22.4620201587677

(II) Teste de memoria

A) Lista

def fibonacci(max):
    sequencia = []
    x,y = 0,1
    while len(sequencia) < max:
        sequencia.append(y)
        x,y = y, x+y
    return sequencia

for x in fibonacci(1000):
    print(x)
    
B) Generator
    
def fibonacci(max):
    x,y,contador = 0,1,0
    while contador < max:
        x,y = y, x+y
        yield x
        contador = contador + 1

for x in fibonacci(1000):
    print(x)
'''


    
