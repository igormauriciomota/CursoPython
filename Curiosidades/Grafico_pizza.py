#----------------------------Desenhar grafico pizza-------------------------------------------

import matplotlib.pyplot as grafico

gols = [55,48,46,12,61,87]
jogadores = ['Messi','CR7','Neymar','Hazard','De Bruyne','Gabigol']

grafico.pie(gols, labels=jogadores)

#grafico.pie(gols, labels=jogadores, autopct='1%1.1f%%')
#grafico.legend()
grafico.savefig("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\pizza.png")
grafico.show()

