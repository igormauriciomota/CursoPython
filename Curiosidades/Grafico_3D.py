"""
Graficos 3D em Python

pip list

"""

import matplotlib.pyplot  # pip install matplotlib
import numpy  # pip install numpy

# Defilição de um grafico tri dimencional x,y,z

x = numpy.outer(numpy.linspace(-2,2,10), numpy.ones(10))
y = x.copy().T
z = numpy.cos(x ** 3 + y ** 2)

eixo = matplotlib.pyplot.axes(projection = '3d') # Definição da projeção
eixo.plot_surface(x,y,z) # Definição da superficie
eixo.set_title('Grafico 3D') # Definição do titulo
matplotlib.pyplot.show() # Mostrando a figura

