'''
1) Crie um programa representando uma calculadora que realiza as operações de multiplicação, divisão, potência 
e fatorial com até dois números. Receba do usuário a operação que deseja fazer e os números escolhidos por ele. 
Implemente uma função para cada operação matemática utilizando os Doctests. Por fim, faça o tratamento de erros 
com try/except/else/finally.

Observação: Utilize o método TDD

'''

def multiplicacao(a,b):
    """
    Define a multiplicação entre dois números
    >>> mutiplicacao(2,3)
    6
    """
    return a * b

def divisao(a,b):
    """
    Determina a divisão entre dois números
    >>> divisao(20,4)
    5.0
    """
    return a / b

def potencia(a,b):
    """
    Determina a Potencia de dois numeros
    >>> potencia(3,2)
    9
    """
    return a ** b

def fatorial(a):
    """
    Determina o fatorial do numero
    >>> fatorial(5)
    120
    """
    b = a - 1
    while b != 0:
        a = a * b
        b = b - 1
    return a

try:
    op = int(input('Digite: \n1 - Multiplcacao\n2 - Divisao\n3 - Potencia\n4 - Fatorial\nOpcao: '))
except ValueError:
    print('Apenas numeros são aceitos')
else:
    try:
        if op == 1:
            resultado = multiplicacao(int(input('Digite o pimeiro valor: ')), int(input('Digite o segundo valor: ')))
            print(f'A operação desejada foi multiplicacao e o resultado é {resultado}')
        elif op == 2:
            resultado = divisao(int(input('Digite o pimeiro valor: ')), int(input('Digite o segundo valor: ')))
            print(f'A operação desejada foi divisao e o resultado é {resultado}') 
        elif op == 3:
            resultado = potencia(int(input('Digite o pimeiro valor: ')), int(input('Digite o segundo valor: ')))
            print(f'A operação desejada foi potencia e o resultado é {resultado}') 
        elif op == 4:
            resultado = fatorial(int(input('Digite o pimeiro valor: ')))
            print(f'A operação desejada foi fatorial e o resultado é {resultado}')
        else:
            print('Operação inválida')
    except ValueError:
        print('Apenas numeros sao aceitos') 
finally: #Finaliza o processo 
    print('Programa Finalizado!')
    
    