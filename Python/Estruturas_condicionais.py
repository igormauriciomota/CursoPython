"""
Estruturas Condicionais

    if(se)
    elif(senão se)
    else(senão)

# Testar altura para brincar do parque

altura = float(input('Digite sua altura: '))

if altura < 1.6:
    print('Voce não pode Bricar!')
else:
    print('Voce pode Brincar!')

# Consultar media final para aprovação
nota = float(input('Digite a sua nota: '))

if nota > 6:
    print('Pode curtir suas férias')
elif nota == 6:
    print('Media Alcançada voce passou')
else:
    print('Te vejo ano que vem outra vez')

# Consultar media final para aprovação
nota1 = float(input('Digite a sua nota etapa 1: '))
nota2 = float(input('Digite a sua nota etapa 2: '))
nota3 = float(input('Digite a sua nota etapa 3: '))

nota_total = nota1 + nota2 + nota3

if nota_total >= 60:
    print('Pode curtir suas férias')
else:
    print('Te vejo ano que vem outra vez')

# Determinar se um numero e par ou impar (Igual ==)
num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'{num} e par')
else:
    print(f'{num} e impar')

# 8 / 4 = 2 resto 0
# 9 / 4 = 2 resto 1

# Determinar se um numero e par ou impar (Diferente !=)
num = int(input('Digite um numero: '))

if num % 2 != 0:
    print(f'{num} e Impar')
else:
    print(f'{num} e Par')

# Utilizar outro tipo de dados - Strings

pais = input('Digite um pais que voce deseja visitar: ')

if pais == 'Noruega':
    print('Ah não, muito frio!')
elif pais == 'China':
    print('Ah não, muito Longe!')
elif pais == 'Australia':
    print('Ah não, muito canguru!')
else:
    print('Vamos!')

# Utilizando outros tipos de dados
# Boolean

login = False
senha = 'caneta1'

key = input('Digite sua senha: ')

# 1º Proco de condicionais
if key == senha:
    login = True
else:
    print('Senha incorreta!')

# 2º Proco de condicionais
if login == True:
    print('Bem vindo admin!')
else:
    print('Tente novamente!')

# Cuidado com as variaveis locais e globais

login = False # Variavel global
senha = 'caneta1'
key = 'caneta1'

# esta variavel local so existe dentro deste bloco
if key == senha:
    login = True # Variavel local
else:
    print('senha incorreta')

# if login == True:
if login:
    print('Bem vindo admin!')
else:
    print('Tente novamente!')


"""

# Cuidado com as variaveis locais e globais

login = False # Variavel global
senha = 'caneta1'
key = 'caneta1'

# esta variavel local so existe dentro deste bloco
if key == senha:
    login = True # Variavel local
else:
    print('senha incorreta')

# if login == True:
if login:
    print('Bem vindo admin!')
else:
    print('Tente novamente!')













