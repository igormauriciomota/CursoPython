'''
Any, All, Max e Min

(I) any: Retorna True se qualquer elemento do iteravel dor True
Obs.: Neste caso, um iteravel vazio retorna False.  

print(any([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True

print(any('Programando Ideias')) # True

print(any([0])) # False

# O resto da divisão de numero 5 e igual zero verdadeiro ou falso
numeros = [1, 2, 3, 4, 5, 6]
print(list(num % 5 == 0 for num in numeros))
print(any(num % 5 == 0 for num in numeros))

[False, False, False, False, True, False]
True

------------------------------------------------------------

(II) All: Retorna True se todos os elementos de iteravel forem verdadeiro
Obs.: Neste caso, um iteravel vazio retorna True []

print(all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # True

print(all('Programando Ideias')) # true

print(all([0])) # False

print(all([0, False, {}, [], (), 89437])) # False / todod tem de ser verdadeiros

print(all([])) # True

numeros = [2, 4, 6, 8, 10, 11]
print(list(num % 2 == 0 for num in numeros))
print(all(num % 2 == 0 for num in numeros))

[True, True, True, True, True, False]
False

obs.: Todos tem de ser verdadeiros se tivel um False o all sera False

-----------------------------------------------------------

(III) Max

numeros = [31, 12, 343, 43, 11, 242, 15]
print(max(numeros))
print(max(31, 12, 343, 43, 11, 242, 15))

cores = {'azul':2,'vermelho':5,'verde':3}
print(max(cores.values())) # 5
print(max(cores)) # Vermelho -> ordem alfabetica

-----------------------------------------------------------

(IV) Min: Retorna o elemento de menor valor de um iteravel ou dos elementos passados como argumentos

numeros = [31, 12, 343, 43, 11, 242, 15] 
print(min(numeros))                       # 11
print(min(31, 12, 343, 43, 11, 242, 15))  # 11

cores = {'azul':2,'vermelho':5,'verde':3}
print(min(cores.values())) # 2
print(min(cores)) # azul

----------------------------------------------------

alunos = ['Pedro', 'Isadora', 'Lucas', 'Camila', 'Samuel']
print(max(alunos)) # Samuel
print(min(alunos)) # Camila

print(max(alunos, key=lambda aluno: len(aluno))) # Isadora
print(min(alunos, key=lambda aluno: len(aluno))) # Pedro

'''



