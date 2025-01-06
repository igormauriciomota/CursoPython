'''
Exercícios:

1) Crie uma função que contenha 3 funções dentro:

- Uma delas deixa a string toda maiúscula.
- Outra que Soma dois números passados pelo usuário.
- E, a ultima soma um numero passado pelo usuário com um numero aleatório entre 0 e 15 com o comando randint().

A função mais externa recebe todos os parâmetros com *args e deve-se fazer
tratamento com try, except caso o usuário passe de forma errada os dados
desejados. A função em args deve receber primeiro o nome da função interna
que deseja acessar e os parâmetros necessários nessa ordem
especificamente. Ex: função_externa(‘soma_num’,2,3), no caso está chamando
a função interna que soma dois números (2,3). Cada função deve imprimir seu
resultado.

1º 


def funcao_externa(*args):
    if args[0] == 'upper_str':
        def upper_str():
            try:
                print(*args[1].upper())
            except AttributeError:
                print('Não tem como aplicar upper() em variaveis que nao sejam str')
        return upper_str

resposta = funcao_externa('upper_str', 'vitoria')
resposta() # V I T O R I A


'''

from random import randint


def funcao_externa(*args):
    if args[0] == 'upper_str':
        def upper_str():
            try:
                print(*args[1].upper())
            except AttributeError:
                print('Não tem como aplicar upper() em variaveis que nao sejam str')
        return upper_str
    elif args[0] == 'soma':
        def soma():
            try:
                print(f'Soma: {args[1] + args[2]}')
            except TypeError:
                print('Deve conter apenas numeros')
            except IndexError:
                print('Deve passar dois numeros como parametros')
        return soma
    elif args[0] == 'soma_maluca':
        def soma_maluca():
            try:
                print(f'Soma maluca: {args[1] + randint(1,15)}')
            except TypeError:
                print('Deve-se conter apenas numeros')
        return soma_maluca
    else:
        def erro():
            print('Nenhuma função chamada')
        return erro
    

resposta = funcao_externa('soma_maluca', 1)
resposta()
resposta = funcao_externa('soma', 1,2)
resposta() # 1 + 2 = 3
resposta = funcao_externa('upper_str', 'vitoria')
resposta() # V I T O R I A
resposta = funcao_externa('oi', 'teste')
resposta()