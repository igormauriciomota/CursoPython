'''
Raise

Tratar erros

- A palavra Eaise significa levantar, em programação e utilizada para apresentar/levantar erros no 
codigo que náo mesmos identificamos 

- A palavra reise é reservada assim com return, def, break,.... 

- Caso voce utilize o 'raise' dentro de uma função, assim que o programa o reconhecer ira acusar o erro e sair da função.  

? como declarar?

raise tipo_do_erro('Mensagem que voce deseja que apareça')

Ex:

A) Cadastramento em um site:

(1º) Fase

# função de cadastro
def cadastrar(login, senha):
    print(f'Login: {login} e Senha: {senha}')
    
#Chamar a função
cadastrar(123, 123)

(2°) Fase

# função de cadastro
def cadastrar(login, senha):
    if type(login) is not str: # is comparação de tipos / == comparação de valores
        raise TypeError('Login deve ser string')
    if type(senha) is not int:
        raise TypeError('Senha deve ser Inteiro')
    print(f'Login: {login} e Senha: {senha}')
    
#Chamar a função
cadastrar('123', 123)

#Chamar a função
cadastrar((input('Digite seu login: ')),int(input('Digite sua senha: ')))

B) numero do divisor

def divisao(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError('Numero 2 não pode ser zero, pois e denominador')
    divisao = num1/num2
    print(f'{divisao}')
    
divisao(int((input('Digite um numero: '))),int(input('digite outro numero: ')))


'''




