'''
Lambdas

- São como funçoes sem nome que funcionan como uma função qualquer

- Sintaxe: lambda parametros: retorno

# Print por dentro 
def pot(x, y):
    print(x ** y)
    
pot(3, 2)

# print por fora

def pot(x, y):
    return x ** y
    
print(pot(3, 2))


# lambda = Expreços lambda aceita qualquer quantidade de parametros de aentrada

(I) Exemplo de expreção lambda

post = lambda x, y: x ** y
print(post(3, 2))

post = lambda x, y: print(x ** y)
post(3, 2)

(II) Exemplo de expreção lambda

cadastro = lambda nome, idade: f'Nome: {nome.title()}\nIdade: {idade}'
print(cadastro('Pedro', 24))

--- ou ----

cadastro = lambda nome, idade: print(f'Nome: {nome.title()}\nIdade: {idade}')
cadastro('Pedro', 24)

Código problemático:

foo = lambda x: x**2 + 2 * x + 1  # [unnecessary-lambda-assignment]

Código correto:

def foo(x):
    return x**2 + 2 * x + 1
    
(III) Exemplo 

a)
segGrau = lambda a, b, c, x: a * x ** 2 + b * x + c
print(segGrau(1, 5, 8, 3))

b) função def conforme lambda;

def quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
segGrau = quadratica(1, 5, 8)
print(segGrau(3))

'''


# Outra forma de fazer o exemplo 3
def quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
segGrau = quadratica(1, 5, 8)
print(segGrau(3))

