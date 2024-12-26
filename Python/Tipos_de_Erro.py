'''
Tipos de erros mais comuns em Python

Tratamento de erros

- Para tratar erros e muito bom prestar atenção na mensagem apresentada no console

Erros mais comuns:

a) AttributeError : Ocorre qunado há falha de atribuição.  
Ex:

dicionario = {'SP':'Sao Paulo', 'RJ': 'Rio de janeiro'}
dicionario.add('ES') # comando add nao exixte em dicionario ('add' = sets-conjuntos)
print(dicionario)

----------------------------------------

b) IndexError: Ocorre quando não exixte o indice de acesso dentro de variavel
EX: IndexError: list index out of range

lista = [1,2,3,4,5]
print(lista[3]) # 4
print(lista[6]) # Erro nao ha indice 6 vai ate o 4

----------------------------------------

c) KeyError: Erro de chaveamento: quando uma chave nao encontrada dentro de um dicionario;

dicionario = {'SP':'Sao Paulo', 'RJ': 'Rio de janeiro'}
print(dicionario['SP'])
print(dicionario['MG']) # Erro chave nao exixte no dicionario

----------------------------------------

d) NameError: Ocorre quando uma variavel ou função não e encontrada no codigo
Ex: Acusa NameError pois nao há declaração da variavel

print(programandoideias)
programandoideias = 'top'

----------------------------------------
e) SyntaxError: surge quando há um erro de sintaxe:

variavel =         # Variavel deve ser declarada
10

break 101          # não pode ter numero depois do break

def variavel = 5   # função deve ser declarada correta (def variavel():)

# 
----------------------------------------

f) IndentationError: Ocorre quando há um erro de identação no codigo

x = 10
if x == 10:
x = 5 # Acusa indentation Error, pois não está identado 4 espaço

----------------------------------------

g) TypeError: Ocorre quando há uma operação com tipos icorretos

Ex: A soma de uma 'String' + um numero concatenação ou soma

nome = 'Igor' # Strig
idade = 39 # Inteiro

nomeIdade = nome + idade
print(nomeIdade) # TypeError: can only concatenate str (not "int") to str

----------------------------------------

h) ValueError: Acontece quando uma função recebe um parametro do tipo certo, mas valor errado
Ex:

Tem de ser digitado um inteiro
ValueError: pois int() tem de ser um valor inteiro nao pode ser letras nem flot

valor = int(input('Digite de 1 a 10: '))
print(valor) # ValueError: invalid literal for int() with base 10: 'oi'

'''

valor = int(input('Digite de 1 a 10: '))
print(valor) 

