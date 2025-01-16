'''
Leitura e Escrita Arquivo CSV

- CSV -> Comma Separated Values: Valores separados por virgula (,)
- pode ser semparados por outros metodos deve obedecer um padrão

Ex:

1,2,3,4,5,6
1:2:3:4:5:6
1;2;3;4;5;6
1 2 3 4 5 6
1-2-3-4-5-6

Serve como ferramente para manipulação de dados;
http://dados.gov.br/dataset

------------------------------------------------------------------------------------------------

(I) Abrindo arquivo CSV para leitura

1 - Modo não usual

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\pessoas_famosas.csv") as arq:
    informacoes = arq.readlines()
    print(type(informacoes))
    print(informacoes)
    for elemento in informacoes:
        print(elemento, end='')
    del informacoes[0]
    print(informacoes)
    for indice, conteudo in enumerate(informacoes):
        print(indice) # Retorna o indice
        print(conteudo) # Retorna o Conteudo
        informacoes[indice] = conteudo.split(',')
    print(informacoes)

['Tom Cruise,Missao Impossivel\n', 'Tom Holland,Homem Aranha\n', 'Emma Watson,Harry Potter\n', 
'Angelina Jolie,Malevola\n', 'Jennifer Aniston,Marley&Eu\n']
0
Tom Cruise,Missao Impossivel
1
Tom Holland,Homem Aranha
2
Emma Watson,Harry Potter
3
Angelina Jolie,Malevola
4
Jennifer Aniston,Marley&Eu

[['Tom Cruise', 'Missao Impossivel\n'], ['Tom Holland', 'Homem Aranha\n'], ['Emma Watson', 
'Harry Potter\n'], ['Angelina Jolie', 'Malevola\n'], ['Jennifer Aniston', 'Marley&Eu\n']]

--------------------------------------------------------------------------------------------------

2 - Modo usual correto Pythonico

# Abrindo para leitura

a) Reader() -> Itera as linhas do arquivo como lista

from csv import reader

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\pessoas_famosas.csv") as arq:
    leitura = reader(arq)
    print(type(leitura)) # <class '_csv.reader'>
    next(leitura)
    for teste in leitura:
        print(teste)

['Tom Cruise', 'Missao Impossivel']
['Tom Holland', 'Homem Aranha']    
['Emma Watson', 'Harry Potter']    
['Angelina Jolie', 'Malevola']     
['Jennifer Aniston', 'Marley&Eu']

--------------------------------------------------------------------------------------------------

from csv import reader

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\pessoas_famosas.csv") as arq:
    leitura = reader(arq)
    print(type(leitura)) # <class '_csv.reader'>
    next(leitura)
    for teste in leitura:
        print(teste)
    arq.seek(0)
    next(leitura)
    for linha in leitura:
        print(f'{linha[0]} participou do filme {linha[1]}')

Tom Cruise participou do filme Missao Impossivel
Tom Holland participou do filme Homem Aranha    
Emma Watson participou do filme Harry Potter    
Angelina Jolie participou do filme Malevola     
Jennifer Aniston participou do filme Marley&Eu 



'''

from csv import reader

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\pessoas_famosas.csv") as arq:
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        print(f'{linha[0]} participou do filme {linha[1]}')
        

