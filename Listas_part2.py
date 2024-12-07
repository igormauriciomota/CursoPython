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

# Utilizando o for para adicionar uma lista
listaNova = []
for numero in range(1, 11):
    listaNova.append(numero)
    
print(listaNova)
# ou assim
listaNova2 = list(range(1, 11))
print(listaNova2)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elemento in lista2:
    print(elemento, end= ' ')

1 2 3 4 5 6 7 8 9 10

# Media da Lista2 [1,2,3,3,4,5,8,8,10]  e 4.888888888888889
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

"""

lista1 = [] # Lista vasia
lista2 = [1,2,3,3,4,5,8,8,10] # Lista de numeros inteiros
lista3 = [3.4, 25.5, 123.566] # Lista de numeros reais
lista4 = [True, False] # Lista de boleanos
lista5 = ['tatu', 'roxo', 'a'] # Lista de string
lista6 = list('Silvio santos 1898')
lista7 = [43, True, 23.2, 'abacate', [1,2,3,]] # diversificada

# While Media da Lista2 [1,2,3,3,4,5,8,8,10]


