'''
Exercícios:
1) Sami e Dudu irão fazer uma competição de quem visita mais Estados no Brasil
em um período de 6 meses, até então Dudu já visitou o Espírito Santo e São
Paulo, enquanto Sami visitou Rio de Janeiro e Bahia. Crie dois conjuntos
diferentes para simbolizar os estados que cada um foi. Após 6 meses Dudu
visitou Bahia, Acre, Santa Catarina e Sergipe, enquanto Sami visitou Bahia,
Minas Gerais, Amazonas e Paraná, atualize cada um dos conjuntos com os
novos Estados. Responda:

- Quais Estados Dudu visitou que Sami não foi?
- Quais Estados ambos foram?
- Sendo 27 Estados no Brasil todo, qual porcentagem o vencedor visitou?

'''
#Situação inicial ao começar o desafio
estados_sami = {'RJ','BA'}
estados_dudu = {'ES','SP'}
sair = ''
while sair != 'nao': #Enquanto sair for diferente de nao faça:
    estados_sami.add(input('Qual Estado Sami visitou a mais? '))
#Adiciono o elemento ao conjunto, lembrando que se for elemento
#repetido ele ignora.
    sair = input('Tem mais Estados a adicionar? ')
sair = ''
while sair != 'nao':
    estados_dudu.add(input('Qual Estado Dudu visitou a mais? '))
    sair = input('Tem mais Estados a adicionar? ')
    
#Quais Estados Dudu visitou que Sami não foi?
print(estados_dudu.difference(estados_sami))
#Difference imprime a diferença entre o conjunto de dudu e sami, logo
#resta apenas os elementos que apenas estã em dudu

#Quais Estados ambos foram?
print(estados_sami.intersection(estados_dudu))
#intersection imprime os elementos em comum dos dois conjuntos

#Qual porcentagem de Estados no Brasil o vencedor visitou?
#A função len retorna a quantidade de elementos dentro do conjunto,
#logo a quantidade de Estados visitados
if len(estados_sami) > len(estados_dudu):
#O calculo len(estados_sami)*100//27 apresenta a porcentagem dos
#estados visitados em relação ao total
    print(f'Sami ganhou e visitou {len(estados_sami)*100 // 27} %')
elif len(estados_dudu) > len(estados_sami):
    print(f'Dudu ganhou e visitou {len(estados_dudu)*100 // 27} %')
else:
    print(f'Deu empate e ambos visitaram: {len(estados_dudu)*100//27}%')
#Poderia ser len(estados_sami)*100//27 também