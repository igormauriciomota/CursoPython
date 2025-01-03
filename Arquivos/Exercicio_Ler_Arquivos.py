'''
Exercicios Ler Arquivos


'''
from random import choice as ch

numerosRifa = []
with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Rifa.txt") as rifa:
    for num in rifa: # Itera em cada linha do arquivo
        numerosRifa.append(int(num)) # int(num) para remover o '\n'

print(f'Número vencedor: {ch(numerosRifa)}. Parabéns!')

