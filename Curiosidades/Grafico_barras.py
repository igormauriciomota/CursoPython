"""
Pacote numpy: https://www.w3schools.com/python/numpy/numpy_intro.asp

- O NumPy tem como objetivo fornecer um objeto de matriz que seja até 50x mais rápido que as listas tradicionais do Python.
- Ele também possui funções para trabalhar no domínio da álgebra linear, transformada de Fourier e matrizes.
- import numpy as np

"""

#----------------------------Desenhar grafico de barras---------------------------------------


import matplotlib.pyplot as grafico
import numpy as np

PES = [10,18,7,32,21]
FIFA = [21,14,12,23,23]
SONY = [9,13,15,20,25]

eixo1 = np.arange(len(PES))
eixo2 = [dist + 0.25 for dist in eixo1]
eixo3 = [dist + 0.25 for dist in eixo2]

# Grafico.bar indica que quer graficos com barras
grafico.bar(eixo1, PES, width=0.25, label='PES', color='blue')
grafico.bar(eixo2, FIFA, width=0.25, label='FIFA', color='green')
grafico.bar(eixo3, SONY, width=0.25, label='SONY', color='red')

paises = ['Brasil','Paraguai','Argentina','Italia','França']
# xticks coloca os paises no eixo (x)
grafico.xticks([dist + 0.25 for dist in range(len(PES))], paises)

grafico.legend()
grafico.title('Vendas dos jogos')
grafico.ylabel('Quantidade em milhares')
# salvar o arquivo em png
#grafico.savefig("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\barras.png")
grafico.show()


