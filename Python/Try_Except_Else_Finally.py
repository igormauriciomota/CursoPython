'''
Tratamento de Error com Try, Except, Else e Finally

Como declarar?

try:
    #Processo
except:
    #Processo
else:
    #Processo
finally:
    #Processo


(I) try & except sempre devem estar juntos

try:               # Tente fazer isso
    #Processo
except:            # Exceto ao apresentar algum error em (try) faça:
    #Processo

(II) else: & finally: são Opcionaris dentro do codigo

else:             # Se não -> "else:"  e usado qunado o "try:" funciona
    #Processo
finally:          # Finalmente faça "Ele sempre vai funcionar sempre e executado"
    #Processo
    
    ---------------------------------------
    
(III) Tratamento de erro na calculadora

A) tratando com try/except:

1 - Tratando de forma generica.

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Mutiplicacao \n 4 - Divisao \n 5 - Exponeciacao \n Opcao:'))
except:
    print('Deu algum erro') # DESTA FORMA ELE E UM DEFOOL NAO PODE SER REPETIDO SE NAO DA ERRO/NAO COLOQUE 
    
2 - Tratamento mais recomendado de forma especifica.

try:
    #processo
excepr (opcional_tipo_de_erro):
    #Processo
    
Exemplo: 
try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Mutiplicacao \n 4 - Divisao \n 5 - Exponeciacao \n Opcao:'))
except ValueError:
    print('Deu ValueError')

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Mutiplicacao \n 4 - Divisao \n 5 - Exponeciacao \n Opcao:'))
except ValueError as erro:
    print(f'Deu {erro}')

# De forma especifica pode ser usado usando cada erro de forma especifica nao pode repetir
try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Mutiplicacao \n 4 - Divisao \n 5 - Exponeciacao \n Opcao:'))
except ValueError as erro:
    print(f'Deu {erro}')
except TypeError as erro:
    print(f'Deu {erro}')
    
    ---------------------------------------
    
B) Tratamento de Error: try/except/else:

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Mutiplicacao \n 4 - Divisao \n 5 - Exponeciacao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:   
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    if operacao == 1:
        print(f'Resultado: {soma(num1,num2)}')
    elif operacao == 2:
        print(f'Resultado: {subtracao(num1,num2)}')
    elif operacao == 3:
        print(f'Resultado: {mutiplic(num1,num2)}')
    elif operacao == 4:
        print(f'Resultado: {divisao(num1,num2)}')
    elif operacao == 5:
        print(f'Resultado: {exponenc(num1,num2)}')

Digitando errado a mensagem e: Deu ValueError

    ---------------------------------------

C) Tratamento de Error: try/except/else/finally:

# finally e muito usado para finalizar processo:

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Mutiplicacao \n 4 - Divisao \n 5 - Exponeciacao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    try:
        num1 = int(input('Digite o primeiro numero: '))
    except ValueError:
        print('Deu erro:')
    else:
        num2 = int(input('Digite o segundo numero: '))

        if operacao == 1:
            print(f'Resultado: {soma(num1,num2)}')
        elif operacao == 2:
            print(f'Resultado: {subtracao(num1,num2)}')
        elif operacao == 3:
            print(f'Resultado: {mutiplic(num1,num2)}')
        elif operacao == 4:
            print(f'Resultado: {divisao(num1,num2)}')
        elif operacao == 5:
            print(f'Resultado: {exponenc(num1,num2)}')
finally:
    print('Processo finalizado!')

'''
# Criando uma CALCULADORA

# Função
# Soma
def soma(x,y):
    op = x + y
    return op

# Subtraçao
def subtracao(x,y):
    op = x - y
    return op

# Mutiplicação
def mutiplic(x,y):
    op = x * y
    return op

# Divisão
def divisao(x,y):
    try:
        op = x / y
    except ZeroDivisionError:
        print('O denominador não pode ser zero')
    else:
        return op

# Esponenciação
def exponenc(x,y):
    op = x ** y
    return op

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n 1 - Soma \n 2 - Subtracao \n 3 - Mutiplicacao \n 4 - Divisao \n 5 - Exponeciacao \n Opcao:'))
except ValueError:
    print('Deu ValueError')
else:
    try:
        num1 = int(input('Digite o primeiro numero: '))
    except ValueError:
        print('Deu erro:')
    else:
        try:
            num2 = int(input('Digite o segundo numero: '))
        except ValueError:
            print('Deu erro!')
        else:
            if operacao == 1:
                print(f'Resultado: {soma(num1,num2)}')
            elif operacao == 2:
                print(f'Resultado: {subtracao(num1,num2)}')
            elif operacao == 3:
                print(f'Resultado: {mutiplic(num1,num2)}')
            elif operacao == 4:
                print(f'Resultado: {divisao(num1,num2)}')
            elif operacao == 5:
                print(f'Resultado: {exponenc(num1,num2)}')
finally:
    print('Processo finalizado!')
    
    