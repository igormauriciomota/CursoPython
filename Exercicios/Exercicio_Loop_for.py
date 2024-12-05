"""
1 - Faça um Programa que calcule a soma dos divisores de um numero inteiro definido pelo usuário
ex. se o usuario escolher 10, temos 1 + 2 + 5 + 10 = 18

soma = 0
numero = int(input('Digite o numero: '))
for num in range(1,numero+1):
    if numero % num == 0:
        soma = soma + num
        print(num)
print(soma)


2 - Faça um programa que imprima os n primeiros multiplos de 5, sendo n definido pelo usuario,
Ex, se o usuario escolheu n=3, sera impresso 5, 10, 15

numero = int(input('Digite o numero de multiplos de 5 que deseja: '))
for num in range(1,numero+1):
      print(f'{5 * num}')

"""
