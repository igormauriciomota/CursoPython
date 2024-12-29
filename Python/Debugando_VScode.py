'''' Para Ativar o modulo debug do VScode:

O que e Debug

- Debug e uma forma de voce limpar e analisar todos os problemas ocorridos no seu codigo
- A prática de utilizar print( ) para tratar erros apresentado aos poucos os dados ao longo do programa
e uma pratica ruim.

1- Clicar no menu executar/iniciar depuração (F5)
2- Selecione "Python File - Debug the currently active Python file
3- Note que abrirá uma aba do lado esquerdo "Executar e Depurar"
4- Antes de executar a depuração vamos selecionar BREAK POINTS
5- Passe o mouse nos números das linhas e observe que aparecerá um sinal vermelho ofuscado
6- Clicar nas linhas que deseja depurar (break-points)
7- E então clicar em "EXECUTAR E DEPURAR"
8- Note o menu de controle que aparece na parte superior direito do vscode
9- Observe:
    a) Play, Next, Return, Avançar, STOP
    b) O menu (lado esquerdo) variaveis. Expanda as variaveis e acompanhe o debug

'''

lista = ['adriano', 'Karina', 'Igor', 'Mota']

for a in lista:
    for b in a:
        c = b.upper()
        
