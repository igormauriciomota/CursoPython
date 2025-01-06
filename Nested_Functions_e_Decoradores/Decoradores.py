'''
Decoradores

O que são Decoradores?

- São funções que voce utiliza para decorar/enfeitar/complementar suas outras funções.   

Como declarar?
- @nome_da_funcao_decoradora

(I) Decorar sem utilizar um decorador;

Ex: 1

def pessoa():
    print('Igor Mota')
    
def motivacao(funcao): # Função decoradora
    def decorando():
        funcao()
        print('Continui em frente')
        print('Voce e o melhor')
        print('Quem dedica sempre alcança')
        print('Carpe diem') # aproveita o momento.
    return decorando

decorada = motivacao(pessoa)
decorada()

Ex: 2

def motivacao(): 
    print('Continui em frente')
    print('Voce e o melhor')
    print('Quem dedica sempre alcança')
    print('Carpe diem') 

def pessoa():
    print('Igor Mota')
    motivacao()

pessoa()

-------------------------------------------------------------------------------

(II) Utilizando o @decorador

# Obs.: Para utilizar a função decoradora, devemos declara-la antes de usar o decorador
    
def motivacao(funcao): # Função decoradora
    def decorando():
        funcao()
        print('Continui em frente')
        print('Voce e o melhor')
        print('Quem dedica sempre alcança')
        print('Carpe diem') # aproveita o momento.
    return decorando


@motivacao # Decorador
def pessoa():
    print('Igor Mota')
    
pessoa() # Ja executa a função/ utilizando o decorador bvasta eu executar a função decorada que já está funcionando;

---> Qual a Vantagem?

- Usando decoradores voce tem o trabalho de criar a função decoradora apenas uma vez e basta chama-la com @
- Melhor visualização caso ocorra um erro
- São comuns em frameworks web(desenvolvimento de sites) como Flask e Bottle

------------------------------------------------------------------------------- 

(III) Passando parametro nos decoradores:

Ex. 1

def calculadora(funcao):
    def decorando(x,y,op):
        print(f'Farei a operação soma de {x} e {y}')
        return funcao(x,y,op)
    return decorando

@calculadora
def soma(num1, num2, op):
    return num1 + num2

print(soma(2,5,1))

-------------------------------------------------------------------------------

Ex. 2 

Mas e se o numero de parametros de entrada for diferente ???
programa com problema: TypeError: calculadora.<locals>.decorando() missing 1 required positional argument: 'op'

def calculadora(funcao):
    def decorando(x, y, z, op): # 'Os parametros dependem de qual função o usuario deseja decorar'
        if op == 1:
            print(f'Farei a operação soma de {x} e {y}')
            return funcao(x,y,op)
        else:
            print(f'Farei a operação soma de {x}, {y} e {z}')
            return funcao(x, y, z, op)
    return decorando

@calculadora
def soma(num1, num2, op):
    return num1 + num2

@calculadora
def mul(num1, num2, num3, op):
    return num1 * num2 * num3

print(soma(2,5,1))
print(mul(2,3,3,2))

-------------------------------------------------------------------------------

Ex. 3 SOLUÇÂO - Basta utilizar *args e **kwargs

- args: retorna uma tupla(imutavel)
- kwargs: retorna um dicionario(chave: dados)


def calculadora(funcao):
    def decorando(*args, **kwargs):
        if len(args) == 2:
            print(f'Farei a operação soma de {args[0]} e {args[1]}')
            return funcao(*args, **kwargs)
        else:
            print(f'Farei a operação multiplicação de {args[0]}, {args[1]} e {args[2]}')
            return funcao(*args, **kwargs)
    return decorando

@calculadora
def soma(num1,num2):
    return num1 + num2

@calculadora
def mul(num1,num2,num3):
    return num1 * num2 * num3

print(soma(2,5))
print(mul(2,3,3))

-------------------------------------------------------------------------------

Dica extra: Forçar parametros com decorador

'''

def obrigando_primeiro_valor(numero):
    def calculadora(funcao):
        def decorando(*args, **kwargs):
            if args[0] == numero:
                if len(args) == 2:
                    print(f'Farei a operação soma de {args[0]} e {args[1]}')
                    return funcao(*args, **kwargs)
                else:
                    print(f'Farei a operação multiplicação de {args[0]}, {args[1]} e {args[2]}')
                    return funcao(*args, **kwargs)
            else:
                return f'O primeiro valor deve ser {numero}'
        return decorando
    return calculadora

@obrigando_primeiro_valor(3)
def soma(num1,num2):
    return num1 + num2

@obrigando_primeiro_valor(3)
def mul(num1,num2,num3):
    return num1 * num2 * num3

print(soma(2,5))
print(mul(2,3,3))

