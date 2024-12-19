'''
Exercícios:

1 - Faça o sistema de uma corrida entre MerCúrio, Papa-Léguas, SoNic, FlaSh,
LiGeirinho e Super Homem (MC, PL, SN, FS, LG, SH). Crie uma função que
receba os 6 corredores em ordem do vencedor até o último (pedir ao usuário),
sendo os três primeiros em variáveis obrigatórias e os três últimos em kwargs,
com as chaves sendo as posições na corrida. Pedir ao usuário se houve
trapaça:

- se não houve: apresentar a classificação final.
- se houve: pedir ao usuário quem trapaceou e quem foi prejudicado. Depois,
trocá-los de posições. Por fim, apresentar a classificação final.

def classParcial(primeiro, segundo, terceiro, **outros):
    op = input('Houve trapaça? s/n: ')
    quarto = ''
    quinto = ''
    ultimo = ''
    
    if op == 'n':
        for posicao, corredor in outros.items():
            if posicao == '4':
                quarto = corredor
            elif posicao == '5':
                quinto = corredor
            elif posicao == '6':
                ultimo = corredor
                
    
        classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo)
    
    elif op == 's':
        colocacao =[primeiro, segundo, terceiro]
        colocacao.extend(outros.values()) # Adiciona a lista os valores do dicionario
        
        babaca = input('Quem trapaceou? : ')
        vitima = input('Quem foi prejudicado? : ')
        
        posBabaca = colocacao.index(babaca) # Retorna os indices dos corredores na lista colocação
        posVitima = colocacao.index(vitima)
        
        colocacao[posBabaca] = vitima
        colocacao[posVitima] = babaca
        
        classFinal(*colocacao) # Descompacta a lista para ser enviada a função 'classFinal'
        
    else:
        print('Digite uma opção valida!')
        
# Criação da 2 função
def classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo):
    print('Classificação Final: ')
    print(f'Primeiro: {primeiro}')
    print(f'Segunto: {segundo}')
    print(f'Terceiro: {terceiro}')
    print(f'Quarto: {quarto}')
    print(f'Quinto: {quinto}')
    print(f'Ultimo: {ultimo}')
    
print('Corredores: ')
print('Mercurio (MC), papa-Leguas (PL), sonic (SN), Flash (FS), Ligeirinho (LG) e Super Homem (SH)')

pri = input('Vencedor: ')
seg = input('Segundo: ')
ter = input('Terceiro: ')
quar = input('Quarto: ')
quin = input('Quinto: ')
ult = input('Ultimo: ')

outros={'4':quar,'5':quin,'6':ult}

classParcial(pri,seg,ter, **outros)



'''
