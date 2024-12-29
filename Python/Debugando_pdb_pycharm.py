'''
O que e Debug

- Debug e uma forma de voce limpar e analisar todos os problemas ocorridos no seu codigo
- A prática de utilizar print( ) para tratar erros apresentado aos poucos os dados ao longo do programa
e uma pratica ruim.

EX:

def boas_vindas(nome):
    print(nome) # Apenas para verificar se a variavel esta certa
    print(f'Seja bem vindo/a {nome}')
    
boas_vindas('Carlos')

# Forma profissional/pytonica para tratar/corrigir erro de codificação

a) PDB: Python Debugger
- Para usar utiliza-lo devemos importar uma biblioteca chamada pdb e assim utilizar a função set_trace()

Há alguns comandos básicos a serem usados no pdb
1) l(list): Apresenta onde voce está no codigo
2) n(next): Pular para a proxima linha
3) p(print): Imprime uma variavel
4) c(continue): continua a execução do codigo até o final do programa ou até o proximo set_trace()

Ex:

import pdb

l = 2
y = 3
pdb.set_trace()
z = l * y
nome = 'Clara'
pdb.set_trace()
frase = nome * z
print(frase)

# cuidado para nao usar letras em seu código quando se confundem com os elementos l/n/p/c

-> z = l * y
(Pdb) p l
2     
(Pdb) 

- Apartir da versão 3.7 do Python não precisa importar pdb, ela foi incorporada aos Built-in com o nome breakpoint()

'''


x = 2
y = 3

z = x * y
nome = 'Clara'
frase = nome * z
print(frase)

