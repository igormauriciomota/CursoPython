"""
1- Fazer uma calculadora de 4 operaçoes (Soma, mutiplicação, divisao inteira, potencia).
Peça a operação desejada e depois os dois numeros ao usuario.

# 1
print('1 - soma\n2 - Multiplicacao\n3 - Divisao Inteira\n4 - Potencia')
op = int(input('Escolha uma operação: '))
nun1 = float(input('Primeiro numero: '))
nun2 = float(input('Segundo numero: '))

if op == 1:
    print(f'soma: {nun1 + nun2}')
elif op == 2:
    print(f'Multiplicacao: {nun1 * nun2}')
elif op == 3:
    print(f'Divisao Inteira: {nun1 // nun2}')
elif op == 4:
    print(f'Potencia: {nun1 ** nun2}')
else:
    print('Digite uma opção Valida!')
    
"""



