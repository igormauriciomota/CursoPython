'''
Dicionarios

a) São apresentados po {}
b) Possuem uma relação chave-> elemento
c) Dicionarios permitem qualquer tipo de dado (int, float, string,....)
d) Não são ordenados
e) São utilizados para otimizar a busca de dados, pois basta voce saber a chave que ira acessar o elemento;

(I) Como declarar?

1-forma (Mais usada):

time_futebol = {'RJ': 'Flamengo', 'SP': 'Corintias', 'MG': 'Cruzeiro'}
print(time_futebol)
print(type(time_futebol))

{'RJ': 'Flamengo', 'SP': 'Corintias', 'MG': 'Cruzeiro'}
<class 'dict'>

2-forma (Utilizando o comando dict()):

times_futebol = dict(RJ='Flamengo', SP='Corintias', MG='Cruzeiro')
print(times_futebol)

3-forma (Menos usada): fronkeys()



'''
# chave = key /Dado = value
times_futebol = {}.fromkeys('[1234]', 'value')
print(times_futebol)
