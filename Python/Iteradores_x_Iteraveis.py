'''
Iteradores x Iteraveis

Definição:

O que e um Iterador?
- È um objeto que pode ser itarado e retorna um dado quando utiliza-se a função next()
O que e um Iteravel?
- E um objeto que retorna um iterador quando usa-se a função iter()

Ex:

nome = 'Programando Ideias' # String são iteraveis como ja vimos
lista = [1, 'oi', True] # Listas são iteraveis

prim_iterador = iter(nome)
segun_iterador = iter(lista)

print(prim_iterador)
print(segun_iterador)
print(type(prim_iterador)) # <class 'str_ascii_iterator'>

- o loop for trabalha exatamente assim, ele pega um itaravel, aplica iter() e assim desmembra a sequencia com varios next()

for i in nome:
    print(i, end=' ') # P r o g r a m a n d o   I d e i a s
    
# next -> Retorna um dado / se imprimir mais do que precisa aparecera Error: StopIteration
    
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))   
print(next(prim_iterador))

P
r
o
g

lista = [1, 'oi', True] # Listas são iteraveis

seg_iterador = iter(lista)
iteradorfinal = iter(seg_iterador) # Comprovando que ao aplicar iter() em um iterador ele se mantem iterador

print(iteradorfinal) # Retorna uma lista iteradora
for i in seg_iterador: # Loop for continua pois ao aplicar o metodo iter() um iterador, ele se mantem iterador
    print(i)

<list_iterator object at 0x0000028D02495B70>
1
oi
True

- Sabendo como funciona iterador e iteravel, nos podemos criar o nosso proprio loop.
ex:

iteravel = [1,2,3,4,5,6,7,8,9,10]
iterador = iter(iteravel)

while True: # loop infinito
    try:
        elemento = next(iterador) # Elemento recebe cada caracter de iteravel que foi transformado em iterador
        print(elemento, end=',')
    except StopIteration:
        break # Para o loop infinito

1,2,3,4,5,6,7,8,9,10,

'''


iteravel = [1,2,3,4,5,6,7,8,9,10]
iterador = iter(iteravel)

while True: # loop infinito
    try:
        elemento = next(iterador) # Elemento recebe cada caracter de iteravel que foi transformado em iterador
        print(elemento, end=',')
    except StopIteration:
        break # Para o loop infinito




