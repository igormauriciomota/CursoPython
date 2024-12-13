'''
Generator Python

- Tuple Comprehension

Gerar um objeto generator a partir do processamento de uma coleção de dados;

sitaxe: (operação/função for elemento in iteravel)



'''
# Exemplos de generators

# exemplo 1

# Class generator
numeros = list(range(1, 11))
maiores = (num for num in numeros if num > 5)
print(type(maiores))
print(maiores) # nao e possivel fazer a impressao <generator object <genexpr> at 0x000002F0F736C5F0>
# e necessario interar
for i in maiores:
    print(i, end=' ')
# objeto generator e perdido, assim que utilizado ele e apagado;

# exemplo 2

nomes = ('Pedro', 'Tiago', 'João', 'Lucas', 'Gustavo')
nome5 = (nome + ('Mota') if len(nome) == 5 else nome for nome in nomes) 
print(type(nome5))
print(nome5)
listaNome = list(nome5)
print(listaNome)

# Comparação de ocupação de memória

from sys import getsizeof

print(getsizeof('Programando Ideias')) # Retorna a memoria ocupada em Bytes
print(getsizeof(10)) # Retorna a memoria ocupada em Bytes
print(getsizeof(123459785315)) # Retorna a memoria ocupada em Bytes
# Tamanho de uma List Comprehension
print(getsizeof([num for num in range(1, 1001)]))

# tamanho de um Generator
print(getsizeof(nun for nun in range(1, 1001)))
