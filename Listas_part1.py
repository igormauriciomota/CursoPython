"""
Lista - Coleção de dados muito poderosa e importante, diferente de tudo que voce já viu,

- Listas - São dinamicas: podem receber qualquer tipo de dado,
    tamanho limitado á memoria disponivel do seu PC.
    
Sintaxe: o que determina uma lista e os "colchetes [elemento1, elemento2, ..... elementoN]" 

Exemplo de Listas

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

# Adicionar valores em uma lista
# Append: Adiciona apenas 1 elemento por vez

print(lista2)
lista2.append(6)
lista2.append(True)
lista2.append([1,2,3,4])
lista2.append('Igor Moa')
print(lista2)

# Adicionar valores em uma lista
# Extend: Adiciona multiplos elementos
- so recebe interavel

lista5.extend(['abacaxi', 1.98, 'kg'])
print(lista5)

['tatu', 'roxo', 'a', 'abacaxi', 1.98, 'kg']

# Adicionar valores em uma lista
# Insert: Adiciona um valor em determinado indice de uma lista
# Obs.: Este comando não substitui o valor original, apenas desloca-o para a direita

lista4.insert(1, 'Aqui')
print(lista4)

[True, 'Aqui', False]

# Concatenar duas (ou mais) listas
listaSoma = lista2 + lista4
print(listaSoma)

[1, 2, 3, 3, 5, 8, 8, 10, True, False]

lista2 = lista2 + lista4
print(lista2)

ou 

lista2.extend(lista4)
print(lista2)


"""

lista1 = [] # Lista vasia
lista2 = [1,2,3,3,5,8,8,10] # Lista de numeros inteiros
lista3 = [3.4, 25.5, 123.566] # Lista de numeros reais
lista4 = [True, False] # Lista de boleanos
lista5 = ['tatu', 'roxo', 'a'] # Lista de string
lista6 = list('Silvio santos 1898')
lista7 = [43, True, 23.2, 'abacate', [1,2,3,]]

cor = 'azul'
animal = 'raposa'
numero = 5
lista8 = [cor, animal, numero]

# 
lista2.extend(lista3)
print(lista2)

