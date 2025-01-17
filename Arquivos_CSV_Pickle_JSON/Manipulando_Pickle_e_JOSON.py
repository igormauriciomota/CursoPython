'''
Manipulação de Pickle e JSON

---------------------------PICKLE---------------------------

- O Objetivo do Pickle é realizar a serialização ou desserialização dos dados recebidos como objeto

- Seu conteudo não é entendivel para a leitura humana

Obs.: Apenas faça a leitura de arquivos quando voce tiver certeza se a fonte é confiavel, 
pois pode conter conteudo malicioso

---- ESCREVER-E-CRIAR----

# Ex: Escrevendo em arquivos pickle

import pickle

class Filme:
    
    def __init__(self, nome, personagem):
        self.__nome = nome
        self.__personagem = personagem
        
        
filme1 = Filme('Senhor dos Aneis', 'Frodo')
filme2 = Filme('Jogos Vorazes', 'Katniss')


with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\filmes.pickle','wb') as arq:
    pickle.dump((filme1, filme2), arq) # dump é usado para criar a serealização do conteudo do objeto (transf Binario)
    
----LEITURA----

import pickle


class Filme:
    
    def __init__(self, nome, personagem):
        self.__nome = nome
        self.__personagem = personagem
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def personagem(self):
        return self.__personagem    

filme1 = Filme('Senhor dos Aneis', 'Frodo')
filme2 = Filme('Jogos Vorazes', 'Katniss')


with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\filmes.pickle','wb') as arq:
    pickle.dump((filme1, filme2), arq) # dump é usado para criar a serealização do conteudo do objeto (transf Binario)
    
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\filmes.pickle','rb') as arq:
    filme1, filme2 = pickle.load(arq) # Load descarrega o arquivo aplicando a desserialização
    print(f'O nome do filme e {filme1.nome} e o personagem e {filme1.personagem}')
    print(f'O nome do filme e {filme2.nome} e o personagem e {filme2.personagem}')

---------------------------------JSON------------------------------------



'''



