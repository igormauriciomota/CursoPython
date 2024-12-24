'''
Any, All, Max e Min

(I) any: Retorna True se qualquer elemento do iteravel dor True
Obs.: Neste caso, um iteravel vazio retorna False.  

print(any([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True

print(any('Programando Ideias')) # True

print(any([0])) # False

# O resto da divisão de numero 5 e igual zero verdadeiro ou falso
numeros = [1, 2, 3, 4, 5, 6]
print(any(num % 5 == 0 for num in numeros))


'''

print(any([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(any('Programando Ideias'))

print(any([0]))

# O resto da divisão de numero 5 e igual zero verdadeiro ou falso
numeros = [1, 2, 3, 4, 5, 6]
print(any(num % 5 == 0 for num in numeros))