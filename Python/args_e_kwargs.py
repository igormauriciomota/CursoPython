'''
*args e **kwargs

- São parametros como quais quer outros
- Não são obrigatorios (não exigem argumentos)
- Seu nome não importa, e sim o asterisco(s)
- Os nomes args e kwargs são apenas por convenção
- Ajudam a evitar erros e retornam a função mais dinamica

---- *args - Gera uma " TUPLA "

Exemplo 1

def cadastro(nome, idade, *args):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    
    print(args)
    print(f'Profissao: ', end=' ')
    for prof in args:
        print(prof, end=' ')
        
cadastro('Agnaldo', 87, 'Carpinteiro', 'Lutador', 'Analista')

Nome: Agnaldo
Idade: 87
('Carpinteiro', 'Lutador', 'Analista')   
Profissao:  Carpinteiro Lutador Analista 

Exemplo 2

def media(*args):
    print(sum(args)/len(args))
    
media(1,2,3,4,5) # Media e 3

# obs.: que ao realizar este formato os valores de peixe passa ser 1 e nun2 recebe o 2, 
# sobrando pra args somete os valores de 3,4,5
def media(peixe, nun2, *args):
    print(sum(args)/len(args))
    
media(1,2,3,4,5) # Media e 4

Exemplo 3 - *args com coleçao de dados

# lista
notas = [8, 9.7, 2.3, 5, 10, 0, 0, 2, 6.9]

def somaNotas(*args):
    print(args)
    print(sum(args))
    
# somaNotas(notas) # TypeError: 
# E reconhecido como uma tupla: ([8, 9.7, 2.3, 5, 10, 0, 0, 2, 6.9],)
# E necessario usar o asterisco (*) no argumento informa que deve haver um desempacotamento da coleçao de dados
somaNotas(*notas) # result 43.9
#somaNotas() Não são obrigatorios (não exigem argumentos)

-> o asterisco(*) no argumento informa que deve haver um desempacotamento da coleçao de dados 
(listas, tuplas, conjuntos), antes que a mesma seja enviada para a função;


---- **kwargs armazena os argumentos EXTRAS E NOMEADOS em um " dicionario "

Exemplo 1

def idade(**kwargs):
    for nome, idade in kwargs.items():
        print(kwargs) # dicionario {'maria': 5, 'isadora': 20, 'pedro': 14}
        print(f'A idade de {nome} e {idade}')
        
idade(maria=5, isadora=20, pedro=14)

Exemplo 2

def jogadas(nome, **kwargs):
    print(kwargs)
    for jogada in kwargs:
        print(kwargs[jogada])
        if kwargs[jogada] == 10:
            return f'{nome} ganhou!'
    return f'{nome} perdeu!'

print(jogadas('Marcelo', j1=9, j2=8, j3=4, j4=10, j5=7)) # Marcelo ganhou!
print(jogadas('Marcelo', j1=9, j2=8, j3=4, j4=6, j5=7) $ Marcelo perdeu!

{'j1': 9, 'j2': 8, 'j3': 4, 'j4': 6, 'j5': 7}
9
8
4
6
7

# Exemplo 1; de **kwargs com dicionario

def apresentarNotas(**kwargs):
    for aluno in kwargs:
        print(f'Nome: {aluno}, nota: {kwargs[aluno]}')
        
notas = {'joão':7,'Igor':8,'jessica':9}

apresentarNotas(**notas)

# Exemplo 2;

def apresentarNotas(joao, carlos, jessica):
        print(f'Joao: {joao}, Carlos: {carlos}, jessica: {jessica}')
        
notas = {'joao': 7, 'carlos': 10, 'jessica': 9} # case sensitive tem de ser igual aos parametros da função;
apresentarNotas(**notas)

-----//-------

# Exemplo 3; ordem de utilização da *args e **kwargs

A - CORRETA: def funçõ(obrigatorios, *args, default, **kwargs)

def certa(nome, *args, cidade='curitiba', **kwargs):
    print(f'{nome}\n{args}\n{cidade}\n{kwargs}')

certa('dudu', 10, 20, 30, 40, estado='Parana', pais='Brasil')

result:

dudu
(10, 20, 30, 40)
curitiba
{'estado': 'Parana', 'pais': 'Brasil'}

------//-----

-> ERRADA: def funçõ(obrigatorios, default, *args, **kwargs) Não usar

# a ordem dos fatores altera o quadrado?

def errada(nome, cidade='curitiba', *args, **kwargs):
    print(f'{nome}\n{args}\n{cidade}\n{kwargs}')

errada('dudu', 10, 20, 30, 40, estado='Parana', pais='Brasil')

dudu
(20, 30, 40)
10
{'estado': 'Parana', 'pais': 'Brasil'}

'''

def certa(nome, *args, cidade='curitiba', **kwargs):
    print(f'{nome}\n{args}\n{cidade}\n{kwargs}')
    
def errada(nome, cidade='curitiba', *args, **kwargs):
    print(f'{nome}\n{args}\n{cidade}\n{kwargs}')
    
certa('dudu', 10, 20, 30, 40, estado='Parana', pais='Brasil')
errada('dudu', 10, 20, 30, 40, estado='Parana', pais='Brasil')



