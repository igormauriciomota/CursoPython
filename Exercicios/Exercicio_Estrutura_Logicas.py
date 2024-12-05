"""
1 - Crie um sistema de cadastro e login de um site, utilizando um username e senha informandos pelo usuário.


# 1
login = False
print('Bem-vindo(a) ao cadastro do site!')
# Coleta os daados 
user = input('Crie seu nome de usuário: ')
senha = input('Crie sua senha: ')

print('\n_________LOGIN__________')
# 01 Etapa - verifica se os dados coletados são iguais ao inseridos em login
if input('Usuario: ') == user and input('Senha: ') == senha: #Testando as duas condiçoes com o 'and'
    login = True


# pode ser usado desta forma

a)

if login:
    print(f'\nBem-vindo(a) {user}')
else:
    print('\nTente novamente!')



# E possivel desenvolver o teste de login de outros modos.
# E utilizando outros operadores, por exemplo.

b)

if not login:
    print('\nTente novamente!')
else:
    print(f'\nBem-vindo(a) {user}')
"""