
"""
Loop While

Como declarar?
While condição: #Enquanto essa condição for True/Verdadeira faça:
    #Processo

EX: 1

x = True
while x:
    print('Estou rodando')
    x = False
    
EX: 2

pedido = ''

while pedido != 'quero sair':
    pedido = input('Voce não vai sair: ')
    
O loop "while" diferente do loop "for", pois precisa de uma condição de parada definida, 
voce tem de determinar esta condição. A palavra (break) executa a finalização do loop while.

EX: 3

contador = 0

while contador < 9:
    print(contador, end = ' ')
    contador = contador + 1
    if contador == 5:
        break # Ira sair do loop imediatamente
        
=> Dicas de ouro:

1) Podemos escrever um loop while em uma mesma linha caso a codificação seja simples:

Ex: 
contador = 0
while contador < 9: print(contador, end = ' '); contador = contador + 1;

2) Palavra continue(Prosseguir):

Ex:
contador = 0

while contador < 9:
    print(contador, end = '')
    contador += 1
    if contador == 5:
        continue
        
                ___ FOR ____                               X               ___WHILE___   
                       
Numero de interaçoes dependente da sua sequencia                   Numero de iteraçoes ilimitados
Utiliza um contador que automaticamente se incrementa              Pode utilizar um contador, porem e becessario que voce declare ele por fora e o incremente por dentro

- Qual dos dois e melhor?
 Ambos são permutaveis, logo voce pode decidir qual queira em determinada situação
 
"""