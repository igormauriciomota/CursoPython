'''
Faça uma funçao que receba um número inteiro maior que zero e retorne a soma de todos os algoritmos,
caso o valor seja negativo retorne 'Numero invalido'

Ex.:
251 = 2 + 5 + 1 = 8


'''

def soma_algarismo(numero):
    divisor = 1
    num_algarismo = 0
    # loop que descobre a quantidade de algarismos;
    while True:
        if (numero // divisor) == 0:
            break
        else:
            num_algarismo += 1
            divisor *= 10
    soma = 0
    # print(num_algarismo) # quantidade de digitos   
    for valor in range(num_algarismo):
        soma = soma + ((numero // (10 ** valor)) % 10)
    return soma

# Ex: como separ os digitos
# 251 // 100 = 2
# 251 // 10 = 25 % 10 = 5
# 251 // 1 = 251 % 10 = 1
            
numero = int(input('Digite um numero: '))
if numero >= 0:
    print(soma_algarismo(numero))
else:
    print('Numero Invalido')

