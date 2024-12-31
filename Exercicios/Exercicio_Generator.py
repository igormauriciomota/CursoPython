'''
Exercícios:

1) Crie uma lista que armazene inteiros de um usuário em um loop até que o
usuário não deseje mais adicionar, trate o erro com try/except caso o usuário
digite uma letra ao invés de um numero. Passe essa lista para uma função
geradora que reconhecerá quais são os números primos dentro da lista
passada inicialmente. Caso seja um numero primo, retorne pelo método yield,
caso contrário passe para o próximo numero. Ao final, imprima os valores
retornados pelo yield em forma de tupla.

(I) Loop Infinito com parada

lista = []
sair = ''
while sair != 'sim':
    # Tratamento de erro:
    try:
        lista.append(int(input('Digite um Numero: ')))
    except ValueError:
        print('Deve ser um numero!')
    sair = input('Deseja parar? ')

'''
# Função (logica que determina os numeros primos)
def primos_list(lista):
    for item in lista:
        divisor = 1 # Variavel divisor
        num_divisor = 0 # Variavel 
        while divisor <= item:
            if item % divisor == 0: # item lista se o resto e igual a 0
                num_divisor += 1
                divisor += 1
            else:
                divisor += 1
        # Teste se e primo ou nao
        if num_divisor == 2:
            yield item
            
        

# Loop While
lista = []
sair = ''
while sair != 'sim':
    # Tratamento de erro:
    try:
        lista.append(int(input('Digite um Numero: ')))
    except ValueError:
        print('Deve ser um numero!')
    sair = input('Deseja parar? ')
    
tuple_primos = tuple(primos_list(lista))
print(f'Tupla contendo todos os numeros primos: {tuple_primos}')


