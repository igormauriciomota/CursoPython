"""
Tipos de graficos

1-grafico.pie() pie - pizza

2-grafico.bar() bar - barra

3-grafico.plot() plot - linhas

4 - grafico.scatter() dispersão - é um tipo de visualização de dados que exibe as relações entre duas variáveis plotadas como 
pontos de dados no plano de coordenadas. Esse tipo de gráfico de dados é usado para verificar se as duas variáveis estão 
correlacionadas entre si, qual é a intensidade dessa correlação e se há grupos distintos nos dados.

5 - grafico.hist() histograma - é um tipo de gráfico de dados que representa a distribuição de frequência dos 
valores de uma variável numérica.

6 - grafico.boxplot() Um gráfico de caixa é um tipo de gráfico de dados que mostra um conjunto de cinco estatísticas 
descritivas dos dados: os valores mínimo e máximo (excluindo os outliers), a mediana e o primeiro e terceiro quartis. 
Opcionalmente, você também pode mostrar o valor médio. Um gráfico de caixa é a escolha certa se você estiver interessado 
apenas nessas estatísticas, sem se aprofundar na distribuição real dos dados subjacentes.

7 - grafico.stackplot() área empilhada é uma extensão de um gráfico de área comum (que é simplesmente um gráfico de linhas 
com a área abaixo da linha colorida ou preenchida com um padrão) com várias áreas, cada uma correspondendo a uma variável 
específica, empilhadas umas sobre as outras. Esses gráficos são úteis quando precisamos monitorar o progresso geral de um 
conjunto de variáveis e a contribuição individual de cada variável para esse progresso. Assim como os gráficos de linha, 
os gráficos de área empilhada geralmente refletem a mudança de variáveis ao longo do tempo.

8 - grafico.heatmap() Mapa de calor - Um mapa de calor é um tipo de visualização de dados em forma de tabela em que cada 
ponto de dados numéricos é representado com base em uma escala de cores selecionada e de acordo com a magnitude do ponto 
de dados no conjunto de dados. A principal ideia por trás desses gráficos é ilustrar possíveis pontos quentes e frios dos 
dados que podem exigir atenção especial.

9 - grafico.stem() gráfico de haste é praticamente outra forma de representar um gráfico de barras, só que, em vez de barras 
sólidas, ele consiste em linhas finas com marcadores (opcionais) em cima de cada uma delas. Embora um gráfico de haste possa 
parecer uma variação redundante de um gráfico de barras, ele é, na verdade, a melhor alternativa quando se trata de 
visualizar muitas categorias. A vantagem dos gráficos de haste em relação aos gráficos de barras é que eles têm uma melhor 
relação entre dados e tinta e, portanto, melhor legibilidade.

"""

#----------------------------Desenhar grafico pizza-------------------------------------------

import matplotlib.pyplot as grafico

gols = [55,48,46,12,61,87]
jogadores = ['Messi','CR7','Neymar','Hazard','De Bruyne','Gabigol']

# Mostra o grafico simples sem os dados de porcentgem
#grafico.pie(gols, labels=jogadores)

# Mostra a porcentagem dentro do grafico/ grafico.pie indica que quer grafico pizza
grafico.pie(gols, labels=jogadores, autopct='%1.1f%%')
#grafico.legend()
grafico.savefig("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\pizza2.png")
grafico.show()

