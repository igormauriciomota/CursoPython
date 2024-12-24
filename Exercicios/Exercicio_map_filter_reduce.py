'''
EXERCICIO map(), filter() e reduce()

1 - Calcule o fatorial de n utilizando loop for, e depois utilizando reduce. O
resultado é o mesmo?

n = int(input('Fatorial de: '))
fat = 1

# o range deve começar pelo nº 1, pois se começar pelo 0, o resultado ao multiplicar seria 0
# e deve terminar em n+1 para o valor de n ser incluido na multiplicação
for i in range(1, n+1):
    fat *= i # Multiplica todos os termos do range.
    
print(f'Fatorial loop for: {fat}')

Ex.: n = 4
range(1, 5) = 1, 2, 3, 4
(1) fat = fat * 1 = 1
(2) fat = fat * 2 = 2
(3) fat = fat * 3 = 6
(4) fat = fat * 4 = 24

1.2- Ultilizando reduce

n = int(input('Fatorial de: '))

from functools import reduce

lista = [1]

lista.extend(range(1, n+1))

fat = reduce(lambda x, y: x * y, lista)
print(f'Fatorial reduce: {fat}')

---------------------------------------------

2 - Realizar o cálculo do IMC através de uma função utilizando map com os
dados fornecidos abaixo sobre peso e altura, e salvar os resultados em outra
lista. Apó isso, aplicar o filter para separar pessoas obesas (IMC > 25).

Dados:
índice 0 das tuplas: peso (kg)
índice 1 das tuplas: altura (m)
listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112,
1.63), (98, 1.59)]

listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (54, 1.56), (69, 1.76), (112,
1.63), (98, 1.59)]

def calculoIMC(amostra):
    imc = amostra[0] / (amostra[1] ** 2)
    return imc

imc = map(calculoIMC, listaAmostras)

resultadoIMC = list(imc)
resultIMC = []

for nun in resultadoIMC:
    resultIMC.append(round(nun))
    
print(resultIMC)

sobrepeso = filter(lambda imc: imc > 25, resultIMC)

print(list(sobrepeso))

Result:

[21, 26, 17, 22, 22, 42, 39]
[26, 42, 39] # Acima do peso
'''

