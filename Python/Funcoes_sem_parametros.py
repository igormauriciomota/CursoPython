'''
Aprendendo Funçoes sem parametros

- O que são funçoes?
> São blocos de codigo que irao executar uma tarefa especifica, podendo ser reutilizavel;
> Tem por papel organizar, diminuir seu programa e facilitar alteraçoes e gerenciamento;
> São declaradas após os comentarios iniciais e imports(se houver);
> Já estudamos algumas funçoes;

a) print()
b) input()
c) type()

como declarar?

def nome(parametros ou não):
    #Processo
    
-> Nessa aula vamos focar sem parametro:

def nome():
    #Processo

Ex.:

a)

def teste_frase(): # Não há parametros de entrada
    print('Estou na função')
    
# Executar sempre com parenteses ()   
teste_frase()
teste_frase()

b) Posso chamar a função onde eu quiser.(for)

def teste_frase(): # Não há parametros de entrada
    print('Estou na função')
for i in range(0,3):
# Executar sempre com parenteses ()   
    teste_frase()
    
c)

def teste_frase(): # Não há parametros de entrada
    print('Estou na função')

-> Quando criar variavel do tipo função, deve ser sem PARENTESES ()
frase = teste_frase 
print(type(frase))
frase()

# Quando utiliza parenteses, chama a execução da função, sem parenteses apenas chama o objeto função;

Ha duas classificação em funçoes:
1) Função com retorno e sem retorno:
- O retorno é utilizado para justamente retornar alguma operação/variavel de dentro da função
- Para isso utiliza-se a pavavra (return)

(I) Função sem retorno

def operacao():
    contador = 60 # Isso é uma variavel local, posu esta dentro da função
    contador += 2
    print(f'Contador = {contador}')
    
print(operacao()) # Quando não há return dentro da função retorna None

(II) Função com retorno

def operacao():
    contador = 60 # Isso é uma variavel local, posu esta dentro da função
    contador += 2
    print(f'Contador = {contador}')
    return contador
    
print(operacao()) # Agora o valor retorna o valor da variavel 62

Obs.: Assim que a função reconhece a palavra return, ela finaliza automaticamente

def operacao():
    contador = 59 # variavel local, posu esta dentro da função
    if contador < 60:
        contador += 2
        return contador
    print(f'Contador = {contador}')
    return contador
    
print(operacao()) # Quando não há return dentro da função retorna None

2) Funções recursivas e nao recursiva:
O que e recursividade?
- Aquilo que se repete indefinidamente, em programação uma funçao recursiva e aquela que retorna ela mesma

# Função não recursiva (Não retorna ela mesma, executada apenas 1 vez)
Ex.:

def celsius_kelvin():
    celsius = int(input('Digite o valor em celsius: '))
    kelvin = celsius + 273
    return kelvin

print(celsius_kelvin())

# Função recursiva - Retorna ela mesma;

def celsius_kelvin():
    celsius = int(input('Digite o valor em celsius: '))
    kelvin = celsius + 273
    print(f'{kelvin}')
    sair =input('Deseja sair? ')
    
    # Condição de parada
    
    if sair == 'sim':
        return 'Acabou!'
    else:
        return celsius_kelvin() # 

print(celsius_kelvin()) # Retornando para ela mesma, lembrando de usar os parenteses;

print(celsius_kelvin())

Obs.: Lembre-se SEMPRE de uma condição de parada na recursividade;
Caso contrario caira em um loop infinito.

'''

def celsius_kelvin():
    celsius = int(input('Digite o valor em celsius: '))
    kelvin = celsius + 273
    print(f'{kelvin}')
    sair =input('Deseja sair? ')
    # Condição de parada
    if sair == 'sim':
        return 'Acabou!'
    else:
        return celsius_kelvin() # 

print(celsius_kelvin())




