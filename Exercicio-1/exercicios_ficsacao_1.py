'''
1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

soma = num1 + num2

print(f'A soma dos dois numeros é: {soma}')

2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

metros = float(input('Digite um valor em Metros: '))

milimetros = metros * 1000

print(f'O Valor em milimetros é: {milimetros}')


3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos '))
segundos = int(input('Digite a quantidade de segundos: '))

total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(f'O total em segundos é, {total_segundos}')

4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a 
porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Digite o valor do salário: '))
percentual_aumento = float(input('Digite a porcentagem de aumento: '))

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento

print(f'O valor do aumento é, R$ {valor_aumento}')
print(f'O novo salário e, R$ {novo_salario}')

5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_mercado = float(input('Digite o preco da mercadoria: '))
percentual_desconto = float(input('Digite o percentual de desconto: '))

valor_desconto = preco_mercado * (percentual_desconto / 100)
preco_final = preco_mercado - valor_desconto

print(f'O valor do desconto e: R$ {valor_desconto}')
print(f'O Preço a pagar e de R$ {preco_final}')


6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

8) Faça agora o contrário, de Fahrenheit para Celsius.

9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim 
como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa 
R$ 60,00 por dia e R$ 0,15 por km rodado.

10) Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 
10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

'''
# 1
# 2
# 3
# 4
# 5

preco_mercado = float(input('Digite o preco da mercadoria: '))
percentual_desconto = float(input('Digite o percentual de desconto: '))

valor_desconto = preco_mercado * (percentual_desconto / 100)
preco_final = preco_mercado - valor_desconto

print(f'O valor do desconto e: R$ {valor_desconto}')
print(f'O Preço a pagar e de R$ {preco_final}')

