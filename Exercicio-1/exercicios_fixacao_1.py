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

distancia = float(input('Digite a distancia a percorrer em KM: '))
velocidade_media = float(input('Digite a velocidade media em km/h: '))

tempo_viagem = distancia / velocidade_media

print(f'O tempo de viagem será de {tempo_viagem} horas')


7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

celsius = float(input('Digite a temperatura em Celsius: '))

fahrenheit = (9 * celsius /5) + 32

print(f'A temperatura em fahrenheit e {fahrenheit}')


8) Faça agora o contrário, de Fahrenheit para Celsius.

fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

celsius = (fahrenheit - 32) * 5 / 9

print(f'A temperatura em Celsius e {celsius}')


9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim 
como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa 
R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorrido = float(input('Digite a quntidade de km percorrido: '))
dias_aluguel = int(input('Digite a quantidades de dias pelo qual o carro foi alugado: '))
preco_diario = float(input('Digite o preço da diaria: '))
preco_km = float(input('Digite o peço do km por litro rodado: '))

preco_a_pagar = (dias_aluguel * preco_diario) + (km_percorrido * preco_km)

print(f'O Preço a pagar é de R${preco_a_pagar}')

10) Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 
10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarro_por_dia = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos_fumando = int(input('Digite a quantidades de anos que voce já fumou: '))

total_cigarros = cigarro_por_dia * (anos_fumando * 365)

minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440

print(f'O total de dias de vida perdidos é de {dias_perdidos}')


11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a 1000.

resultado = 2 ** 1000

quantidade_digitos = len(str(resultado))

print(f'A quantidade de digitos em 2 elevado a mil é {quantidade_digitos}')

'''


