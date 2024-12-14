'''
Dicionarios parte 2

ex:
Funcionarios:

Paula, 27 anos, Programadora
Gabriel, 30 anos, Engenheiro

1) listas

funcionarios = []
lista1 = ['Paula', 27, 'Programadora']
lista2 = ['Gabriel', 30, 'Engenheiro']
funcionarios.append(lista1)
funcionarios.append(lista2)
print(funcionarios)
# quiser saber da idade da paula
print(funcionarios[0][1])

result: [['Paula', 27, 'Programadora'], ['Gabriel', 30, 'Engenheiro']]
27

2) Tuplas

tuple1 = ('Paula',27,'Programadora')
tuple2 = ('Gabriel',30,'Engenheiro')
funcionarios = (tuple1,tuple2)
print(funcionarios)
print(funcionarios[1][1])

result: (('Paula', 27, 'Programadora'), ('Gabriel', 30, 'Engenheiro'))
30

3) Dicionario

funcionario = []
dict1 = {'nome':'Paula','idade':27,'funcao':'Programadora'}
dict2 = {'nome':'Gabriel','idade':30,'funcao':'Engenheiro'}
funcionario.append(dict1)
funcionario.append(dict2)
print(funcionario)
print(funcionario[0]['idade'])

result: [{'nome': 'Paula', 'idade': 27, 'funcao': 'Programadora'}, {'nome': 'Gabriel', 'idade': 30, 'funcao': 'Engenheiro'}]
27

ou usar 

funcionario = {}
dict1 = {'nome':'Paula','idade':27,'funcao':'Programadora'}
dict2 = {'nome':'Gabriel','idade':30,'funcao':'Engenheiro'}
funcionario['Paula'] = dict1
funcionario['Gabriel'] = dict2
print(funcionario)
print(funcionario['Paula']['idade'])

4) Metodo - clear() limpar

dicionario = {'Programando':'Ideias'}
dicionario.clear()
print(dicionario)

result: {}

5) Deep copy
Deep copy(Copia profunda): copy
Ex: Cada dicionario trabalha separadamente

dicionario = {'Programando':'Ideias'}
novo = dicionario.copy()
novo['Melhor'] = 'do Mundo'
print(novo)
print(dicionario)

6) Shallow copy(Cópia superficial):
Ex: Não separa cada dicionario ao ser manipulado

dicionario = {'Programando':'Ideias'}
novo = dicionario
novo['Melhor'] = 'do Mundo'
print(novo)
print(dicionario)

7) E possivel iterar dicionarios:

personagem = {'Nome': 'Rick', 'Fincao': 'Cientista', 'Neto':'Morty'}
for item in personagem:
    print(item) # Retorna as chaves
for item in personagem:
    print(personagem[item]) # Retorna as os dados em cada chave
    
8) Método - Keys(): Retorna uma lista com as chaves

personagem = {'Nome': 'Rick', 'Fincao': 'Cientista', 'Neto':'Morty'}
print(personagem.keys()) 

9) Metodo - values(): Retorna uma lista com elementos do dicionario

personagem = {'Nome': 'Rick', 'Fincao': 'Cientista', 'Neto':'Morty'}
print(personagem.values())

10) Método items(): retorna uma lista onde cada indice e uma tupla de chave e dado, 

personagem = {'Nome': 'Rick', 'Fincao': 'Cientista', 'Neto':'Morty'}
print(personagem.items())

dict_items([('Nome', 'Rick'), ('Fincao', 'Cientista'), ('Neto', 'Morty')])

personagem = {'Nome': 'Rick', 'Fincao': 'Cientista', 'Neto':'Morty'}
print(personagem.items())
for item in personagem.items():
    print(item)
    
Posso desmembrar tambem 

personagem = {'Nome': 'Rick', 'Fincao': 'Cientista', 'Neto':'Morty'}
print(personagem.items())
for chave,dado in personagem.items():
    print(chave)
    print(dado)
    
11) metodo len() tamanho do dicionario

personagem = {'Nome': 'Rick', 'Fincao': 'Cientista', 'Neto':'Morty'}
print(len(personagem))

12) Aceita apenas dados numericos

Maximo: max()
Minimo: min()
Somatorio: sum()

dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(max(dict1.values()))
print(min(dict1.values()))
print(sum(dict1.values()))

Lembre-se de usar o metodo values() ou keys() caso queira os elementos nas chaves ou dados
'''

    