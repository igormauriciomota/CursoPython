'''
Exercícios:
1 - Crie 3 listas: uma com o nome de 3 companhias aéreas, e as outras duas
representando o número de passageiros por companhia em dois voos: voo1 e
voo2. Utilize zip(), lambda e map() para obter o valor máximo de passageiros
por companhia nos dois voos e associar estes valores com o nome das
companhias, formando uma lista de tuplas. Por fim, utilizar filter() e lambda
para determinar a classificação da companhia, conforme indicado nos dados
abaixo.

Dados:

0 < Passageiros <= 100: 1 estrela.
100 < Passageiros <= 200: 2 estrelas.
200 < Passageiros <= 300: 3 estrelas.


'''

companheia = ['Gol', 'Latam', 'Azul']
voo1 = [115, 95, 110]
voo2 = [195, 80, 225]

voos1e2 = zip(voo1, voo2) # Junta os numeros de passageiros de cada companhia
# Determina o valor max de passageiros por companhia entre os voos 1 e 2
maxPass = map(lambda voos: max(voos), voos1e2)

listamaxPass = list(maxPass)

compMax = zip(companheia, listamaxPass)
listacompMax = list(compMax)

# Filtra a companhia aérea que tem menos de 100 passageiros em seu valor maximo e depois converte o resultado para uma lista
umaEst = list(filter(lambda valMax: valMax[1] < 100, listacompMax)) 
# Filtra a companhia aérea que tem menos de 200 passageiros em seu valor maximo e depois converte o resultado para uma lista
duasEst = list(filter(lambda valMax: valMax[1] > 100 and valMax[1] <= 200, listacompMax))
# Filtra a companhia aérea que tem menos de 200 passageiros em seu valor maximo e depois converte o resultado para uma lista
tresEst = list(filter(lambda valMax: valMax[1] > 200 and valMax[1] <= 300, listacompMax))

print(f'Uma estrela: {umaEst[0][0]} - Max Passageiro: {umaEst[0][1]}')
print(f'Duas estrela: {duasEst[0][0]} - Max Passageiro: {duasEst[0][1]}')
print(f'Tres estrela: {tresEst[0][0]} - Max Passageiro: {tresEst[0][1]}')

