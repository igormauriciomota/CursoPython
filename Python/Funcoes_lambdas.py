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

# Exemplo 1 de expreção lambda
post = lambda x, y: x ** y
print(post(3, 2))

post = lambda x, y: print(x ** y)
post(3, 2)

# Exemplo 2 de expreção lambda
cadastro = lambda nome, idade: f'Nome: {nome.title()}\nIdade: {idade}'
print(cadastro('Pedro', 24))


'''


# Exemplo 2 de expreção lambda
cadastro = lambda nome, idade: print(f'Nome: {nome.title()}\nIdade: {idade}')
cadastro('Pedro', 24)

