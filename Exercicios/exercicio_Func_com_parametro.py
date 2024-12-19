'''
Exercícios funçoes com parametro:

1 - Criar uma função recursiva (que retorne ela mesma) para armazenar N
termos da sequência de Fibonacci em uma lista. N é definido pelo usuário. Ao
encontrar os termos, imprimir a lista e finalizar a função.

listaSF = []
stop = 0

def fibonacci(stop, a, b, aux):
    global listaSF
    listaSF.append(a) # Adiciona os valores na lista 'listaSF'
    a, b = b, a + b # Acumula os valores para determinar os proximos numeros da sequencia
    # Essa e a logica da sequencia de fibonacci, o proximo termo e sempre a soma dos dois termos anteriores
    aux += 1
    if stop == aux:
        print(listaSF)
        return 0
    else:
        return fibonacci(stop, a, b, aux) # chama a propria função até que stop == aux.
    
while stop < 1:
        stop = int(input('Digite a quantidade de termos: '))
        
fibonacci(stop, a=1, b=1, aux=0 )

------------------------------------

2 - Criar 5 funções: uma para um cadastro, outra para realizar o login, outra
para mudar a senha, outra para realizar logout e ainda uma para definir qual
opção o usuário deseja escolher.
Utilize um loop while para sair do sistema apenas se o usuário desejar (criar a
opção 'sair').

Atente-se às regras:

- Só é possível realizar um cadastro se não houver nenhum anterior.
- Só é possível realizar login se houver um cadastro.
- Só é possível realizar login se o usuário informar corretamente username e senha.
- Só é possível alterar a senha se o usuário estiver logado.
- Só é possível alterar a senha se o usuário informar corretamente a senha atual.
- Só é possível realizar logout se o usuário estiver logado.

'''



