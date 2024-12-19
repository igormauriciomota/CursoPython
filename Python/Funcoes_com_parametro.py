'''
Funções com Parametro:

- Recebem dados e variaveis são chamados de (argumentos) para utilização wm pecessos internos

- Porem ter inumeros parametros (separados por virgula)

Ex.: De funçoes com oarametros

sum()
max()
min()
index()
print()
input()

1 Exemplo:

def imparPar(numero):
    if numero % 2 == 0:
        print(f'{numero} é par')
        #return f'{numero} é par'
    else: 
        print(f'{numero} é impar')
        #return f'{numero} é impar'
        
#print(imparPar(int(input('Digite um numero: '))))
imparPar(10)

2 Exemplo: Calculadora

# Soma
def soma(num1, num2):
    print(num1 + num2)
# Subtração
def subtracao(num1, num2):
    print(num1 - num2)
# Divisão
def divisao(num1, num2):
    print(num1 // num2)
# Mutiplicação
def mutiplicacao(num1, num2):
    print(num1 * num2)
# Elevado
def elevado(num1, num2):
    print(num1 ** num2)
n1 = int(input('Digite o Primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

soma(n1, n2)
subtracao(n1, n2)
divisao(n1, n2)
mutiplicacao(n1, n2)
elevado(n1, n2)

3 Exemplo: Lista

def separar(lista):
    for num in lista:
        if num > 10:
            print(num, end=' ')
            
listaCriada = [21, 2, 3, 4, 9, 50, 48, 49, 11, 21, 535, 45, 875]
separar(listaCriada)

# 21 50 48 49 11 21 535 45 875

4 Exemplo: Nomear argumentos

def cidade(parte1, parte2):
    print(parte1 + ' ' + parte2)
    
cidade(parte1 = (input('Digite um Nome: ')), parte2 = (input('Digite um Nome: ')))

a) Funçoes que nao exige parametros

print()
input()

b) Funão que exige parametros

def soma(num1, num2):
    print(num1 +  num2)
    
soma(10, 18)

c) Função com parametro padrão (default)

Obs.: O parametro padrao deve ser sempre o ultimo entre os parametros de uma função,

-> não pode ser o primeiro ( def medida(numero=60, referencia): Erro: )

def medida(numero, referencia=60):
    if numero > referencia:
        print(f'{numero} e maior que {referencia}')
    else:
        print(f'{numero} e menor que {referencia}')
# medida(int(input('Digite um numero:')))
medida(30, 40) 

- ou usando assim->

def medida(numero=75, referencia=60):
    if numero > referencia:
        print(f'{numero} e maior que {referencia}')
    else:
        print(f'{numero} e menor que {referencia}')
# medida(int(input('Digite um numero:')))
medida()
medida(30, 40)   
medida(70)
medida(20)

75 e maior que 60
30 e menor que 40
70 e maior que 60
20 e menor que 60

d) Variaveis locais e globais para funçoes:
Palavra chave (global) se nao usar vai dar erro:

nome = 'arroz'

def comida():
    global nome
    nome = nome + ' e miojo'
    print(nome)

comida()

exemplo 2

def comida(nome='arroz'):
    nome = nome + ' e miojo'
    print(nome)

comida()

# Comando nonlocal (para funçoes dentro de funçoes)

def funFora():
    total = 0
    def funDentro():
        nonlocal total # nonlocal sem ele da erro e nao e reconhecido a variavel
        total = total + 1
        print(total)
    return funDentro()

funFora()

----//-----

def funFora():
    total = 0
    def funDentro():
        nonlocal total # nonlocal sem ele da erro e nao e reconhecido a variavel
        total += 1    # += 1
        print(total)
    return funDentro()

funFora()

'''

def funFora():
    total = 0
    def funDentro():
        nonlocal total
        total += 1
        print(total)
    return funDentro()

funFora()