"""
Plotando Graficos

o importar matplotlib.pyplot, importamos esta coleção de funções, que inclui as funções:

plot(): Cria um gráfico de linha ou gráfico de dispersão.
hist(): Cria um histograma.
scatter(): Cria um gráfico de dispersão.
bar(): Cria um gráfico de barras.
pie(): Cria um gráfico de pizza.
xlabel(): define o rótulo para o eixo x.
ylabel(): define o rótulo para o eixo y.
title(): Define o título do gráfico.
legend(): Adiciona uma legenda ao gráfico.
xlim(): Define os limites para o eixo x.
ylim(): Define os limites para o eixo y.

"""
#----------------------------Desenhar grafico de linha----------------------------------------

import statistics

import matplotlib.pyplot as grafico

pontuacao = [7,11,10,10,9,12,10,14,18,21,20,24,19,24,18,11,16,12,31,29,38,41,45,53,55]

medias = []
soma = []

for num in pontuacao:
    soma.append(num)
    medias.append(statistics.mean(soma))
    
grafico.ylabel('Pontuação')
grafico.xlabel('Geração')
# valores dos eixos
grafico.axis([0,25,5,60])
# Vai indicar a cor 'b' blu-azul e 'r--' red-vermelha -- pontilhada
grafico.plot(pontuacao, 'g--', medias,'r--')
# grafico.plot(pontuacao,'g^','ys','ro',medias,'r--')
grafico.savefig("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\teste.png")
grafico.show()



















