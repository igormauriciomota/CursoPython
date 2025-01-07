'''
Exercícios:

1) Faça uma função que calcule a diferença entre dois números, decore-a com
outra função a partir das Mensagens: ‘Inicio do Programa’ e ‘Decorando a
funcao’. Após isso faça com que o decorador permita que apenas seja calculada
a diferença positiva entre os dois números, independente da ordem de entrada.
Imprima o resultado.

'''


def completa(funcao):
    def decora(x,y):
        print('-----Inicio do Programa-----')
        print('-----Decorando a Função-----')
        if x > y:
            funcao(x,y)
        else:
            funcao(y,x)
    return decora
    
@completa
def diminui(num1,num2):
    print(f'O resultado desejado: {num1 - num2}')
    
diminui(7,1)
diminui(1,7)