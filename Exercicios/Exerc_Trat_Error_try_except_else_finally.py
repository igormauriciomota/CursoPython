'''
Exercicio 

Tratamento de Error com Try, Except, Else e Finally
    
1-Aplique o procedimento try/except/else/finally no seguinte codigo que realiza um cadastro de formulario
para pessoas realizarem uma viagem
    
'''

opcoes_viagem = {1:'EUA',2:'França',3:'Japão',4:'Brasil'}
try:
    nome = input('Digite seu nome: ')
    teste = int(nome) # transformei a variavel nome em um int
except ValueError:
    try:
        idade = int(input('Digite sua Idade: '))
    except ValueError:
        print('Idade deve conter apenas numeros')
    else:
        try:
            lugar = int(input('Digite o numero para a escolha do lugar: \n 1 - EUA \n 2 - França \n 3 - Japão \n 4 - Brasil \n'))
        except TypeError:
            print('Deus erro!')
        except KeyError:
            print('KeyError: A chave digitada nao cadastrada!')
        else:
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            pais = opcoes_viagem[lugar]
            print(f'viagem marcada para: {pais}')
finally:
    print('Processo finalizado!')
    
    