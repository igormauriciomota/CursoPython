"""
(II) Exemplo de Listas part 2

Obs.: Todas as listas são ordenadas, ou seja seus indices são importantes.  

lista1 = [] # Lista vasia
lista2 = [1,2,3,4,5,6,7,8,9,10] # Lista de numeros inteiros
lista3 = [3.4, 25.5, 123.566] # Lista de numeros reais
lista4 = [True, False] # Lista de boleanos
lista5 = ['tatu', 'roxo', 'a'] # Lista de string
lista6 = list('Silvio santos 1898')
lista7 = [43, True, 23.2, 'abacate', [1,2,3,]] # diversificada

1) Utilizando o for para adicionar uma lista
listaNova = []
for numero in range(1, 11):
    listaNova.append(numero)
    
print(listaNova)
 ou assim
listaNova2 = list(range(1, 11))
print(listaNova2)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elemento in lista2:
    print(elemento, end= ' ')

1 2 3 4 5 6 7 8 9 10

2) Media da Lista2 [1,2,3,3,4,5,8,8,10]  e 4.888888888888889
total = 0
for elemento in lista2:
    total = total + elemento # total recebe 0 + 1 (primeiro elemento) depois total vira 1 + 2 que e o segundo elemento
print(total/len(lista2))

# While Media da Lista2 [1,2,3,3,4,5,8,8,10]

total = 0
cont = 0
while len(lista2) != 0:
    total = total + lista2.pop() # .pop() vai retirar um elemento da lista por vez ate 0
    cont = cont + 1
print(total/cont)

4.888888888888889
[]

3) Obter indice da lista
jogos = ['Sonic', 'Super Mario', 'GTA', 'Gow', 'PES']
for indice, jogo in enumerate(jogos):
    print(indice, jogo)
    
0 Sonic
1 Super Mario
2 GTA        
3 Gow        
4 PES

4) .index() encontrar 

lista2 = [1,2,3,3,4,5,8,8,10] # Lista de numeros inteiros
#print(lista2.index(4))
print(lista2.index(2)) # valor 2 esta no indice 1
print(lista2.index(5, 4)) # Busca a partir do indice 4
print(lista2.index(5, 20)) # ValueErro - 
print(lista2.index(5, 3, 6)) # Busca ENTRE os indices 3 e 6
print(lista8.index(5, 4, 8)) # Busca ENTRE os indices 4 e 8


ValueError: not enough values to unpack (expected 4, got 3)
# ERROS que podem apresentar por utrapassar o numeros de variaveis dentro de uma lista

lista5 = ['tatu', 'roxo', 'a']

animal, cor, letra, numero = lista5
print(animal)
print(cor)
print(letra)
print(numero)

lista5 possui somente tres indices, tem de ter o valor exato.

5) Funçoes úteis para trabalhar com listas
# Obs.: Apenas para inteiros ou floats

sum() - retorna a soma dos elementos
max() - mauior valor
min() - menor valor

print(sum(lista8)) # sum() - retorna a soma dos elementos
print(max(lista8)) # max() - mauior valor
print(min(lista8)) # min() - menor valor

print(sum(lista2))
print(max(lista2))
print(min(lista2))

6) round() Função que arredonda os valores da lista

listaPlana = [1.22, 2.984367, 9.23184832]

for elemento in listaPlana:
    print(round(elemento))

7) abs() Obter o modulo de uma lista/ transfoma negativo em positivo

listaPessimista = [-1, -2, -5, -10, 1000]
for numero in listaPessimista:
    print(abs(numero))
    
8) Deep Copy - Copiar uma lista
Obs.: A deep copy copia as listas e as torna independentes entre si, ou seja,
qual quer modificação em uma NÂO afeta a outra.  

print(lista2)
lista1 = lista2.copy() # copiar o conteudo da lista2 para a lista1
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)
lista1.append(12)
print(lista1)

lista1 = []
lista1 = [1, 2, 3, 3, 4, 5, 8, 8, 10]
lista1 = [1, 2, 3, 3, 4, 5, 8, 8, 10, 11]
lista1 = [1, 2, 3, 3, 4, 5, 8, 8, 10, 11, 12]

9) Shallow Copy - Copiar as lista e as conecta, uma modificação em uma afeta a outra.  

print(lista2)
lista1 = lista2
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)

10) Matrizes em Python e uma lista de lista
    Obs.: cada lista interna e uma linha da matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

print(matriz[0])
print(matriz[1])
print(matriz[2])

indice 0 [1, 2, 3]
indice 1 [4, 5, 6]
indice 2 [7, 8, 9]

ou usar o for

for linha in matriz:
    print(linha)
    
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

print(matriz[0][2]) indice 0 item 2 resutado = 3
print(matriz[1][1]) indice 1 item 1 resutado = 5
print(matriz[2][2]) indice 2 item 2 resutado = 9

for linha in matriz:
    for numero in linha:
        print(numero)

# pega todos os numeros

# Matriz jogo da velha

matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # Matriz 3x3

print(matriz[0])
print(matriz[1])
print(matriz[2])

LP1 = int(input('Escolha a linha: '))
CP1 = int(input('Escolha a coluna: '))
matriz[LP1][CP1] = 'X'

LP2 = int(input('Escolha a linha: '))
CP2 = int(input('Escolha a coluna: '))
matriz[LP2][CP2] = 'O'

for linha in matriz:
    print(linha)
    
"""

lista1 = [] # Lista vasia
lista2 = [1,2,3,3,4,5,8,8,10] # Lista de numeros inteiros
lista3 = [3.4, 25.5, 123.566] # Lista de numeros reais
lista4 = [True, False] # Lista de boleanos
lista5 = ['tatu', 'roxo', 'a'] # Lista de string
lista6 = list('Silvio santos 1898')
lista7 = [43, True, 23.2, 'abacate', [1,2,3,]] # diversificada
lista8 = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]


# Matriz jogo da velha

matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # Matriz 3x3

print(matriz[0])
print(matriz[1])
print(matriz[2])

LP1 = int(input('Escolha a linha: '))
CP1 = int(input('Escolha a coluna: '))
matriz[LP1][CP1] = 'X'

LP2 = int(input('Escolha a linha: '))
CP2 = int(input('Escolha a coluna: '))
matriz[LP2][CP2] = 'O'

for linha in matriz:
    print(linha)
    