'''
Manipulação de Data e Hora em Python parte 2

----MANIPULANDO HORA-----


import datetime

jogo = datetime.time(16,0,0)
print(jogo) # 16:00:00


----FORMATAR-DATA-E-HORA-BRASIL # strftime() existe uma tabela de formatação

import datetime

horaAtual = datetime.datetime.now()
print(horaAtual) # 2025-01-19 18:47:22.423992
horaAtual_BR = horaAtual.strftime('%d/%m/%y') 
print(horaAtual_BR) # 19/01/25

horaAtual = datetime.datetime.now()
print(horaAtual) # 2025-01-19 18:47:22.423992
horaAtual_BR = horaAtual.strftime('%d/%b/%y')
print(horaAtual_BR) # 19/Jan/25

horaAtual = datetime.datetime.now()
print(horaAtual) # 2025-01-19 18:47:22.423992
horaAtual_BR = horaAtual.strftime('%d de %B de %y')
print(horaAtual_BR) # 19 de January de 25

---DIAS-DA-SEMANA---

Obs.: os numeros representam a semana
0 segunda-feira
1 terça-feira
2 quarta-feira
3 quinta-feira
4 sexta-feira
5 sabado
6 o Domingo

import datetime

horaAtual = datetime.datetime.now()
print(horaAtual) # 2025-01-19
print(horaAtual.weekday()) # 6 Domingo

---TEMPO-DE-EXECUÇÂO---

import timeit

numQuadrado = str([x ** 2 for x in range(1000)])
print(timeit.timeit(numQuadrado, number=100)) # 0.0011223999899812043

'''

