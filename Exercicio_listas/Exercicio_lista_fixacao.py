"""
Exercicios Listas

Os comandos para listas em Python incluem:

list.append(x): Adiciona um elemento ao final da lista 
list1.extend(list2): Adiciona um grupo de elementos ao final da lista ou concatena listas 
list.insert(índice, elemento): Insere um elemento em uma posição específica da lista 
list.remove(elemento): Exclui a primeira ocorrência de um elemento da lista 
pop(): Retorna e remove o último elemento da lista 
pop(pos): Retorna e remove o elemento na posição pos da lista 
len(): Retorna o comprimento da lista 
lista.count(elemento): Retorna quantas vezes o elemento aparece na lista 
lista.sort(lista): Ordena o conteúdo da lista 
sum(): Calcula a soma de todos os elementos de uma lista 

1 - Criar uma lista de quadrados de números de 0 a 9

quadrados = [x + 2 for x in range(10)]
print(quadrados)

quadrados = [x * 2 for x in range(10)]
print(quadrados)

quadrados = [x - 2 for x in range(10)]
print(quadrados)

quadrados = [x / 2 for x in range(10)]
print(quadrados)

quadrados = [x ** 2 for x in range(10)]
print(quadrados)

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

2 - Filtrar números pares de 0 a 20

pares = [x for x in range(21) if x % 2 ==0]
print(pares)

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# y % 2 != 0 verifica se o número não é divisível por 2 (ou seja, se o resto da divisão por 2 não é zero), 
# caracterizando um número ímpar.

impares = [y for y in range(21) if y % 2 != 0]
print(impares)

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

3 - Criar uma lista de strings com as primeiras letras dos nomes

# Explicação: O índice [0] seleciona a primeira letra de cada nome
nomes = ['Ana', 'Carlos', 'Beatriz', 'David']

primeiras_letras = [nome[0] for nome in nomes]
print(primeiras_letras)

4 - Dobrar os números de 1 a 5

# Explicação: A expressão x * 2 multiplica cada número de 1 a 5 por 2.
numero = [x * 2 for x in range(1, 6)]
print(numero)

[2, 4, 6, 8, 10]

numero1 = [x * 4 for x in range(2, 12)]
print(numero1)

numero2 = [x * 5 for x in range(5, 21)]
print(numero2)

[25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

5 - Converter uma lista de strings para maiúsculas

# Explicação: O método upper() converte cada palavra para maiúsculas.

palavras = ['python', 'comprehension', 'list', 'programação']
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)

6 - Criar uma lista de números ímpares de 1 a 30

numeros = [x for x in range(31) if x % 2 != 0]
print(numeros)

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

7 - Criar uma lista de quadrados de números negativos

numeros_negativos = [-x for x in range(1, 11)]

quadrados_negativos = [-x ** 2 for x in range(-1, -6, -1)]

cubos_negativos = [x ** 3 for x in numeros_negativos]

print(f'Numeos negativos: {numeros_negativos}')
print(f'Quadrados negativos; {quadrados_negativos}')
print(f'Cubos negativos: {cubos_negativos}')

8 - Extrair números com mais de 3 dígitos
Objetivo: Filtrar e criar uma lista de números com mais de 3 dígitos.

numero = [10, 150, 2000, 30, 50000]
grandes = [x for x in numero if len(str(x)) > 3]
print(grandes)

[2000, 50000]

9 - Criar uma lista de cubos de números

Objetivo: Criar uma lista com o cubo de números de 1 a 10.
cubos = [x ** 3 for x in range(1, 11)]
print(cubos)

[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

10 - Filtrar palavras que começam com a letra "a"

# Objetivo: Criar uma lista com palavras que começam com "a"
palavras = ['abacaxi', 'banana', 'avelã', 'maçã', 'goiaba', 'aveia', 'graviola']
a_palavras = [p for p in palavras if p.startswith('a')]
print(a_palavras)
['abacaxi', 'avelã', 'aveia']

11 - Inverter as palavras de uma lista
Objetivo: Criar uma lista com as palavras invertidas.

palavras = ['python', 'java', 'csharp', 'javaScript']
invertidas = [p[::-1] for p in palavras]
print(invertidas)

['nohtyp', 'avaj', 'prahsc', 'tpircSavaj']

12. Criar uma lista de números divisíveis por 3
Objetivo: Criar uma lista de números divisíveis por 3 de 0 a 50.

13. Contar o número de caracteres em cada palavra
Objetivo: Criar uma lista com a quantidade de caracteres de cada palavra.

14. Criar uma lista de valores booleanos verificando se o número é positivo
Objetivo: Criar uma lista de valores booleanos que indicam se cada número de uma lista é positivo.

15. Converter temperaturas de Celsius para Fahrenheit
Objetivo: Criar uma lista convertendo temperaturas de Celsius para Fahrenheit.

16. Criar uma lista com os quadrados de números ímpares
Objetivo: Criar uma lista com o quadrado de números ímpares de 1 a 10.

17. Criar uma lista de tuplas com números e seus quadrados
Objetivo: Criar uma lista de tuplas, onde cada tupla contém um número e seu quadrado.

18. Filtrar números maiores que 10 e menores que 50
Objetivo: Criar uma lista com números maiores que 10 e menores que 50.

19. Criar uma lista com as letras de uma palavra em ordem inversa
Objetivo: Criar uma lista com as letras de uma palavra, mas em ordem inversa.

20. Criar uma lista de números de 1 a 100 que são múltiplos de 3 e 5
Objetivo: Criar uma lista com números de 1 a 100 que são múltiplos de 3 e 5.

"""

