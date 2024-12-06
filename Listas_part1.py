"""
Lista - Coleção de dados muito poderosa e importante, diferente de tudo que voce já viu,

- Listas - São dinamicas: podem receber qualquer tipo de dado,
    tamanho limitado á memoria disponivel do seu PC.
    
Sintaxe: o que determina uma lista e os "colchetes [elemento1, elemento2, ..... elementoN]" 

(I) Exemplo de Listas

lista1 = [] # Lista vasia
lista2 = [1,2,3,4,5,6,7,8,9,10] # Lista de numeros inteiros
lista3 = [3.4, 25.5, 123.566] # Lista de numeros reais
lista4 = [True, False] # Lista de boleanos
lista5 = ['tatu', 'roxo', 'a'] # Lista de string
lista6 = list('Silvio santos 1898')
lista7 = [43, True, 23.2, 'abacate', [1,2,3,]] # diversificada

# Variavel
cor = 'azul'
animal = 'raposa'
numero = 5
lista8 = [cor, animal, numero]


1) Append.: Adiciona apenas 1 elemento por vez

print(lista2)
lista2.append(6)
lista2.append(True)
lista2.append([1,2,3,4])
lista2.append('Igor Moa')
print(lista2)


2) Extend.: Adiciona multiplos elementos
- so recebe interavel

lista5.extend(['abacaxi', 1.98, 'kg'])
print(lista5)

['tatu', 'roxo', 'a', 'abacaxi', 1.98, 'kg']


3) Insert.: Adiciona um valor em determinado indice de uma lista
# Obs.: Este comando não substitui o valor original, apenas desloca-o para a direita

lista4.insert(1, 'Aqui')
print(lista4)

[True, 'Aqui', False]

4) Concatenar duas (ou mais) listas
listaSoma = lista2 + lista4
print(listaSoma)

[1, 2, 3, 3, 5, 8, 8, 10, True, False]

lista2 = lista2 + lista4
print(lista2)

ou 

lista2.extend(lista4)
print(lista2)

5) split.: Converter string em listas, cria uma lista separando uma string por seus espaços (' ')

frase = 'Hoje e um novo dia, de um novo tempo, que começou'

lista9 = frase.split()
print(lista9)

['Hoje', 'e', 'um', 'novo', 'dia,', 'de', 'um', 'novo', 'tempo,', 'que', 'começou']

lista9 = frase.split(',')
print(lista9)

['Hoje e um novo dia', ' de um novo tempo', ' que começou']

6) join.: Converte listas em strings, cria uma string juntando os elementos de uma lista

lista10 = ['silvio', 'santos', 'vem', 'ai']
frase = ' '.join(lista10)
print(frase)

silvio santos vem ai

7) len().: contar a quantidade de elementos de uma lista

print(len(lista7))

8) Verificar se determinado valor está em uma lista;

if 'x' in lista7:
    print('x esta na lista')
else:
    print('x não esta na lista')
    
ou 

if 12 in lista7:
    print('esta na lista')
else:
    print('não esta na lista')
    
    ou
    
print(40 in lista7)
resultado:    true/false

9) .count().: Obter a quantidade de vezes que um valor se repete em uma lista

print(lista6)
quantidade = lista6.count('8')
print(f'Eu encontrei {quantidade} vez/vezes')

['S', 'i', 'l', 'v', 'i', 'o', ' ', 's', 'a', 'n', 't', 'o', 's', ' ', '1', '8', '9', '8']
2x

print(lista6)
quantidade = lista6.count('s')
print(f'Eu encontrei {quantidade} vez/vezes')

2x obs.: python e case sensitive obs letras maiuscula de minuscualas

10) .sort() - Ordenar uma lista

# Ordenar uma lista
listaMaluca = [10, 9, 8, 7, 6, 21, 232, 123, 434, 1, 83, 42, 18, 2, 15, 3]
print(listaMaluca)

listaMaluca.sort()
print(listaMaluca)

[1, 2, 3, 6, 7, 8, 9, 10, 15, 18, 21, 42, 83, 123, 232, 434]

# Ordenar String

lista_ordenar = ['Igor', 'Amanda', 'Barbara', 'Lisbet', 'Juvenal', 'Cris', 'Daniel', 'Ester']
print(lista_ordenar)

lista_ordenar.sort()
print(lista_ordenar)

['Amanda', 'Barbara', 'Cris', 'Daniel', 'Ester', 'Igor', 'Juvenal', 'Lisbet']

11) .reverse() Inverter uma lista

lista7 = [43, True, 23.2, 'abacate', [1,2,3,], 'x', False, 12]
lista7.reverse()
print(lista7)

result invertido: [12, False, 'x', [1, 2, 3], 'abacate', 23.2, True, 43]

ou - print(lista7[::-1]) # slicing

12) slicing lista[inicio:fim:passo]
            0    1     2       3          4      5     6    7
# lista7 = [43, True, 23.2, 'abacate', [1,2,3,], 'x', False, 12]

print(lista7[2:]) # Do indice 2 ao final
print(lista7[2:6]) # Do indice 2 ao 6
print(lista7[2:7:2]) # Do indice 2 ao 7 de dois em dois elementos

result;
[23.2, 'abacate', [1, 2, 3], 'x', False, 12]
[23.2, 'abacate', [1, 2, 3], 'x']
[23.2, [1, 2, 3], False]

lista7 = [43, True, 23.2, 'abacate', [1,2,3,], 'x', False, 12]

print(lista7[2])
print(lista7[4])
print(lista7[-2])
print(lista7[-4])
print(lista7[5])

for ind in range(0, 3):
    print(lista7[ind])
    
lista7 = [43, True, 23.2, 'abacate', [1,2,3,], 'x', False, 12]

for ind in range(0, 8):
    print(f'Indice: {ind}, valor: {lista7[ind]}')
    
Indice: 0, valor: 43
Indice: 1, valor: True
Indice: 2, valor: 23.2
Indice: 3, valor: abacate
Indice: 4, valor: [1, 2, 3]
Indice: 5, valor: x        
Indice: 6, valor: False    
Indice: 7, valor: 12

13) substituir elemento de uma lista

print(lista7)
lista7[1] = False
lista7[4] = 'Vodka'
print(lista7)

result: 

[43, True, 23.2, 'abacate', [1, 2, 3], 'x', False, 12]
[43, False, 23.2, 'abacate', 'Vodka', 'x', False, 12]

14) pop.: Remover elementos de uma lista e retornao ultimo elemento de uma lista

print(lista2)
print(lista2.pop())
print(lista2)

lista2 = [1, 2, 3, 3, 5, 8, 8, 10]
retirado n° 10
[1, 2, 3, 3, 5, 8, 8]

# È possivel indicar indice do valor a ser removido

print(lista7)
lista7.pop(5)
print(lista7)

exemplo.: x removido elemento 5

[43, True, 23.2, 'abacate', [1, 2, 3], 'x', False, 12]
[43, True, 23.2, 'abacate', [1, 2, 3], False, 12]

# Repetir elementos de uma lista
lista4 = [True, False] # Lista de boleanos
print(lista4)
lista4 = 5 * lista4
print(lista4)

15) .clear() tem a função de Limpar uma lista

print(lista7)
lista7.clear()
print(lista7)

Lista7 = [43, True, 23.2, 'abacate', [1, 2, 3], 'x', False, 12]
lista7 = []

"""

lista1 = [] # Lista vasia
lista2 = [1,2,3,3,5,8,8,10] # Lista de numeros inteiros
lista3 = [3.4, 25.5, 123.566] # Lista de numeros reais
lista4 = [True, False] # Lista de boleanos
lista5 = ['tatu', 'roxo', 'a'] # Lista de string
lista6 = list('Silvio santos 1898')
lista7 = [43, True, 23.2, 'abacate', [1,2,3,], 'x', False, 12]

cor = 'azul'
animal = 'raposa'
numero = 5
lista8 = [cor, animal, numero]

lista10 = ['silvio', 'santos', 'vem', 'ai']
frase = ' '.join(lista10)
print(frase)

