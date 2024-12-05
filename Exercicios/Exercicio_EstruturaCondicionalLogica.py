
"""
1 - Crie um programa que encontre e imprima as raizes de uma equação do segundo grau,
utilizando o metodo de Bhaskara.

# 1
# Equação do segundo grau: A * x ** 2 + B * x + c

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b ** 2) - (4 * a * c) # Encontrando o valor de delta

# Formula de Bhaskara / raiz quadrada e a mesma coisa que elevar ele a meio (0.5)
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print(f'As raizes são: {x1} e {x2}')

- Outro modo de ser realizada a potencia e utilizando o modulo math de Matematica:
ex:

import math

x1 = (-b + math.sqrt(delta)) / (2 * a)

"""


