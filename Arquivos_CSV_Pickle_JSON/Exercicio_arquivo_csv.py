'''
Exercicio 

1) Um time de futsal formado pelo arquivo atletas.csv, que contém nome, altura(cm) e 
peso(kg) de cada esportista, deseja fazer uma pesquisa e saber quais atletas tem altura 
superior a 170 cm e que possui peso menor que 80 kg, imprima o nome deles. Dois reforços 
entraram para o time no início da temporada, Roberto, 175, 77kg e Adriana, 165, 60kg. Atualize 
o arquivo adicionando os jogadores e leia-o novamente.

"C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\atletas.csv"

'''

from csv import reader, writer

with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\atletas.csv") as arq:
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        if int(linha[1]) > 170 and int(linha[2]) < 80:
            print(linha[0])
            
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\atletas.csv','a+', newline ='') as arq:
    escrita = writer(arq)
    escrita.writerow(['Roberto', '175', '77'])
    escrita.writerow(['Adriana', '165', '60'])
    arq.seek(0)
    leitura = reader(arq)
    next(leitura)
    for linha in leitura:
        print(linha)
    