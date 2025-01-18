'''
Manipulação de Data e Hora em Python

- È utilizado o módulo integrado datetime;

- O formato padrão de data e o formato americano: aaaa/mm/dd = ano/mes/dia

Exemplo. 1

import datetime

horarioAtual = datetime.datetime.now() # now() é possivel trabalhar com fuso horário
print(horarioAtual) # 2025-01-18 13:47:19.859774
print(type(horarioAtual)) # <class 'datetime.datetime'>

horarioAtual = datetime.datetime.today()
print(horarioAtual) # 2025-01-18 13:47:19.859774
print(type(horarioAtual)) # <class 'datetime.datetime'>

---------------------------------------------------

Exemplo. 2

import datetime

print(repr(datetime.datetime.now())) # (2025, 1, 18, 13, 52, 58, 860725)
print(dir(datetime)) # Funçãoes ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', 
#'__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 
#'timedelta', 'timezone', 'tzinfo']

---------------------------------------------------

Exemplo. 3

import datetime

print(repr(datetime.datetime.now())) # (2025, 1, 18, 13, 52, 58, 860725)
print(dir(datetime)) # 

print(datetime.MAXYEAR) # 9999 - Ano Maximo
print(datetime.MINYEAR) # 1 -  Ano Minimo

-------Elementos-------data---e---hora

Exemplo. 4 Todos os elementos dadata e da hora

import datetime

# Variavel
horarioAtual = datetime.datetime.now()
print(repr(horarioAtual))

print(horarioAtual.year) # Ano
print(horarioAtual.month) # Mes
print(horarioAtual.day) # Dia
print(horarioAtual.hour) # horas
print(horarioAtual.minute) # Minuto
print(horarioAtual.second) # Segundo
print(horarioAtual.microsecond) # microsegundos

datetime.datetime(2025, 1, 18, 14, 14, 39, 294220)
2025
1   
18  
14  
14  
39
294220

---------------------------------------------------

Exemplo. 5

- Ajustar Data e Hora

import datetime

horarioAtual = datetime.datetime.now()
print(horarioAtual)
horarioAtual = horarioAtual.replace(year=1500, month=4, day=22, hour=10, minute=30, second=0,microsecond=0)
print(horarioAtual) # 1500-04-22 10:30:00

---------------------------------------------------

Exemplo. 6

import datetime

dataUsuario = input('Escolha uma data (dd/mm/aaaa): ')
dataUsuario = dataUsuario.split('/') # separar pela barra
print(dataUsuario)
dataUsuario = datetime.datetime(int(dataUsuario[2]), int(dataUsuario[1]), int(dataUsuario[0]))
print(dataUsuario)

---------------------------------------------------

Exemplo. 7 Delta de data e Hora

import datetime

horarioAtual = datetime.datetime.now()
print(horarioAtual)
fimSeculo = datetime.datetime(2100, 12, 31, 23, 59, 59)
print(fimSeculo)
tempoRestante = fimSeculo - horarioAtual
print(f'Restam {tempoRestante.days} dias para virar o seculo!') # Restam 27740 dias para virar o seculo!
print(f'Restam {tempoRestante.days / 365} anos para virar o seculo!') # 76 anos

------------------Delta-------------------------

# Privisão futura

import datetime

horarioAtual = datetime.datetime.now()
print(horarioAtual)
tempoTrabalho = datetime.timedelta(30) # 30 dias
primeiroSalario = horarioAtual + tempoTrabalho
print(primeiroSalario)

'''

import datetime

horarioAtual = datetime.datetime.now()
print(horarioAtual)
tempoTrabalho = datetime.timedelta(30) # 30 dias
primeiroSalario = horarioAtual + tempoTrabalho
print(primeiroSalario)


