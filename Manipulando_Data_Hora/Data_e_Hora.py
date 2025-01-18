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

Exemplo. 2

import datetime

print(repr(datetime.datetime.now())) # (2025, 1, 18, 13, 52, 58, 860725)
print(dir(datetime)) # Funçãoes ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', 
#'__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 
#'timedelta', 'timezone', 'tzinfo']

Exemplo. 3

import datetime

print(repr(datetime.datetime.now())) # (2025, 1, 18, 13, 52, 58, 860725)
print(dir(datetime)) # 

print(datetime.MAXYEAR) # 9999 - Ano Maximo
print(datetime.MINYEAR) # 1 -  Ano Minimo


Exemplo. 4



'''

import datetime

horarioAtual = datetime.datetime.now()

