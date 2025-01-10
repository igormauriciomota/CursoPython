'''
Python Avançado

Nested functions = Funções dentro de funções

a) Criar uma variavel do tipo função:

def aniversariates(lista_nomes):
    for nome in lista_nomes:
        print(f'Feliz Aniversario {nome}!')
        
        Feliz Aniversario Lucas!
        Feliz Aniversario Vitoria!
        
felicitacoes = aniversariates # Não utilize parenteses() pois assim voce estará executando a função
felicitacoes(['Lucas', 'Vitoria'])
print(type(felicitacoes)) # <class 'function'>
print(felicitacoes) # <function aniversariates at 0x000001E85579A340>

b) Passando funções como argumento/parametro:

from random import randint


def num_aleatorio():
    return randint(1,6)

def pessoa(funcao, nome):
    resultado = funcao()
    if resultado < 4:
        return str(resultado) + ' Voce Perdeu! ' + nome
    else:
        return str(resultado) + ' Vitoria Perfeita! ' + nome

nome = input('Escreva um nome: ')
print(pessoa(num_aleatorio, nome))

c) Retornando uma função dentro de função

Ex1:

from random import randint


def pessoa(nome):
    def num_aleatorio():
        return randint(1,6)
    return f'{nome} tirou {num_aleatorio()}'


print(pessoa(input('Digite um nome: ')))
#print(num_aleatorio()) # Dara NameError pois quando uma função está dentro de outra, ela não e reconhecida externamente

Ex2:

from random import randint

def pessoa():
    def num_aleatorio():
        return randint(1,6)
    return num_aleatorio

print(pessoa()) # imprime a função num_aleatorio em si -> <function pessoa.<locals>.num_aleatorio at 0x000001BB9798D080>
# Criar uma variavel por fora
funcao = pessoa()
print(funcao()) # Lembras dos parenteses (), que tem a função de chamar a função

d) Parametros passados para funções externas são reconhecidas em funçãoes internas:

from random import randint


def pessoa(nome):
    def num_aleatorio():
        return f'{nome} tirou {randint(1,6)}'
    return num_aleatorio

funcao = pessoa('Davila')
print(funcao()) # Parenteses () chama a função/ imprime o nome mesmo não sendo passado como parametro para num_aleatorio


'''
from random import randint


def num_aleatorio():
    return randint(1,6)

def pessoa(funcao, nome):
    resultado = funcao()
    if resultado < 4:
        return str(resultado) + ' Voce Perdeu! ' + nome
    else:
        return str(resultado) + ' Vitoria Perfeita! ' + nome

nome = input('Escreva um nome: ')
print(pessoa(num_aleatorio, nome))
