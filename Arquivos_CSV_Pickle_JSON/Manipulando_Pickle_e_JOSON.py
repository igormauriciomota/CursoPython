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

JSON -> JavaScript Object Notation

- Utilizado em API´s -> Interface de Programação de aplicativos

site com exemplos de JSON: http://jsonapi.org/ 

Ex. 1: dumps() -> Faz a formatação para o formato JSON ("Aspas duplas")

import json

nome = {'Ana':'30 anos'}
teste_json = json.dumps(nome)
print(teste_json)
print(type(teste_json))

{"Ana": "30 anos"}
<class 'str'>

------------JUNTOS---JSON---PICKLE----------

Em Python, podemos trabalhar com json e pickle juntos

No terminal instale: pip install jsonpickle

import jsonpickle


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
print(jsonpickle.encode(filme1)) # encode() é utilizado para criar um dicionario no formato JSON
# O primeiro elemento apresenta qual classe pertence esse objeto
# {"py/object": "__main__.Filme", "_Filme__nome": "Senhor dos Aneis", "_Filme__personagem": "Frodo"}

# Escrevendo arquivos 
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\filmes.json','w') as arq:
    arq.write(jsonpickle.encode(filme1))

-----LENDO---JSON---PICKLE----------

import jsonpickle

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

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\filmes.json') as arq:
    leitura = jsonpickle.decode(arq.read())
    print(leitura)
    print(leitura.nome)
    print(leitura.personagem)

<__main__.Filme object at 0x00000196D5D4E990>
Senhor dos Aneis
Frodo


'''


        
    
    