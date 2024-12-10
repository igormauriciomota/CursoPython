'''
List Comprehensions

Apartir de list Comprehensions e possivel Gerar uma lista a partir do processamento de uma coleção de dados

sintaxe: [operação/função 'for' dentro da lista elemento in iterável]


(I) Exemplo usando loop for

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

pares = []
for num in impares:
    pares.append(num * 2)
print(pares)

(II) Exemplo usando Comprehensions

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

pares = [num * 2 for num in impares]
print(pares)

reult.: [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42]

(III) Comprehensions

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# Leitura ( for num in impares) - para cada "num" em impares/ mutiplique por 2x
print([num * 2 for num in impares])

# Comprehensions

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
pares = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42]

# Leitura for num in impares - para cada "num" em impares/ mutiplique por 2x
pares = [num * 2 for num in impares]
print(pares[5]) # indice 5 dos numeros pares
print(sum(pares)) # Soma dos pares

# (IV) List Comprehensions com estruturas condicionais pode usar o if e else

1) if
# lista de 1 a 10
numeros = list(range(1, 11))

# sintaxe - o if vai na frente do for sempre
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(pares)
print(impares)

2) Else
# lista de 1 a 10
numeros = list(range(1, 11))

# sintax - o else vai atras do for sempre
# num menor ou maior ate 5 e o numeros restante mutiplica por 10
nova = [num if num <+ 5 else num * 10 for num in numeros]

print(nova)
# result.: [1, 2, 3, 4, 50, 60, 70, 80, 90, 100]

(V) List Comprehensions em matrizes

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(num, end=' ') for num in linha] for linha in matriz]

matriz2 = [[num * 3 for num in linha] for linha in matriz]
print(f'\n{matriz2}')

'''
