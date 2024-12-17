'''
Exercícios:
1) Para cada número par em um range de 1 a 9, adicione esse número elevado
ao quadrado no conjunto, se o número for ímpar adicione 2 elementos, 1 por vez:
‘Sou’, ’Impar’. Qual foi a resposta? Por que ‘Sou’, ‘Impar’ só apareceu uma vez?

conjunto = set({}) # somente desta forma vai reconhecer que se trata de um conjunto

Ex.: normal 

conjunto = set({})
for numero in range(1,10):
    if numero % 2 == 0:
        conjunto.add(numero ** 2)
    else:
        conjunto.add('Sou')
        conjunto.add('Impar')
print(conjunto)

Ex.: Set comprehension

conjunto = {numero ** 2 if numero % 2 == 0 else 'sou' 'impar' for numero in range(1,10)}
print(conjunto)

'''
conjunto = {numero ** 2 if numero % 2 == 0 else 'sou' if num == 0 else 'impar' for num in range(0,2) for numero in range(1,10)}
print(conjunto)
