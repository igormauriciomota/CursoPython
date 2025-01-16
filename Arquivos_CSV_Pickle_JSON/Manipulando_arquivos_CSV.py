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

-----------------------------LEITURA--------------------------------------------

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

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\pessoas_famosas.csv",encoding='utf-8') as arq:
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        print(f'{linha[0]} participou do filme {linha[1]}')

Tom Cruise participou do filme Missao Impossivel
Tom Holland participou do filme Homem Aranha    
Emma Watson participou do filme Harry Potter    
Angelina Jolie participou do filme Malevola     
Jennifer Aniston participou do filme Marley&Eu 

--------------------------------------------------------------------------------------------------

from csv import reader

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\animais.csv",encoding='utf-8') as arq:
    leitura = reader(arq, delimiter='/') # Caso haja outro separador
    next(leitura)
    for linha in leitura:
        print(f'O animal {linha[0]} e do tipo {linha[1]}')
        
--------------------------------------------------------------------------------------------------

b) DictReader(): Itera as linhas do arquivo csv como Dicionarios

from csv import DictReader

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\pessoas_famosas.csv",encoding='utf-8') as arq:
    leitura = DictReader(arq)
    print(leitura)
    for teste in leitura:
        print(teste) # Retorna um dicionario

{'Pessoa': 'Tom Cruise', 'Filme': 'Missao Impossivel'}
{'Pessoa': 'Tom Holland', 'Filme': 'Homem Aranha'}    
{'Pessoa': 'Emma Watson', 'Filme': 'Harry Potter'}    
{'Pessoa': 'Angelina Jolie', 'Filme': 'Malevola'}     
{'Pessoa': 'Jennifer Aniston', 'Filme': 'Marley&Eu'}

--------------------------------------------------------------------------------------------------

from csv import DictReader

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\pessoas_famosas.csv",encoding='utf-8') as arq:
    leitura = DictReader(arq)
    print(leitura)
    for teste in leitura:
        print(teste) # Retorna um dicionario
    arq.seek(0)
    next(leitura)
    for linha in leitura:
        print(f"{linha['Pessoa']} participou do filme {linha['Filme']}")


Tom Cruise participou do filme Missao Impossivel      
Tom Holland participou do filme Homem Aranha
Emma Watson participou do filme Harry Potter
Angelina Jolie participou do filme Malevola
Jennifer Aniston participou do filme Marley&Eu

-----------------------------ESCRITA----------------------------------------


(II) Abrindo arquivo CSV para escrita

1 FORMA - writer(): Permite a escrita em csv usando listas

Obs.: writerow() ->

----------------------------

newline='' usado para nao pular linhas no aquivo

from csv import writer

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\animais.csv",'w', newline='', encoding='utf-8') as arq:
    escrita = writer(arq)
    escrita.writerow(['Animal', 'Tipo']) # Adiciona o cabeçalho
    for numero in range(0,2):
        animal = input('Digite o nome do animal: ')
        tipo = input('Digite o tipo do animal: ')
        escrita.writerow([animal, tipo]) # Adiciona os nomes
        
----------------------------

---- delimiter = ':' ou delimiter = '/' entre outros

from csv import writer

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\animais.csv",'w', newline='', encoding='utf-8') as arq:
    escrita = writer(arq, delimiter = ':')
    escrita.writerow(['Animal', 'Tipo']) # Adiciona o cabeçalho
    for numero in range(0,2):
        animal = input('Digite o nome do animal: ')
        tipo = input('Digite o tipo do animal: ')
        escrita.writerow([animal, tipo]) # Adiciona os nomes

----------------------------------ESCRITA---------------------------------------

2 FORMA -

DictWriter() - 

from csv import DictWriter

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\animais.csv",'w', newline='', encoding='utf-8') as arq:
    titulos = ('Animal', 'Tipo')
    escrita = DictWriter(arq,delimiter='/',fieldnames = titulos)
    escrita.writeheader() # serve para adicionar os titulos como primeira linha
    for item in range(2):
        animal = input('Digite o nome do animal: ')
        tipo = input('Digite o tipo do animal: ')
        escrita.writerow({'Animal':animal,'Tipo':tipo}) # nomeclatura das chaves devem ser identicas ao que tem nos titulos


'''

from csv import DictWriter

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\animais.csv",'w', newline='', encoding='utf-8') as arq:
    titulos = ('Animal', 'Tipo')
    escrita = DictWriter(arq,delimiter='/',fieldnames = titulos)
    escrita.writeheader() # serve para adicionar os titulos como primeira linha
    for item in range(2):
        animal = input('Digite o nome do animal: ')
        tipo = input('Digite o tipo do animal: ')
        escrita.writerow({'Animal':animal,'Tipo':tipo})

        
        
    


