'''
1) Deseja-se criar um programa que deixe a formula secreta da coca cola
criptografada, para isso crie uma classe FormulaCocaCola com atributos
privados: ingrediente, temperatura (Celsius), açúcar (gramas) e o nome do
proprietário. Crie uma senha de acesso escolhida pelo usuário, instancie o
objeto e passe o mesmo para um arquivo PICKLE. Após isso, peça a senha
para acessar os atributos, caso esteja correta, leia o arquivo e imprima-os, se
não imprima um aviso de acesso negado.

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\filmes.json')

'''

import pickle


class Formulacocacola:
    
    def __init__(self, ingrediente, temperatura, acucar, proprietario):
        self.__ingrediente = ingrediente
        self.__temperatura = temperatura
        self.__acucar =acucar
        self.__proprietario = proprietario
    
    @property
    def ingrediente(self):
        return self.__ingrediente
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @property
    def acucar(self):
        return self.__acucar
    
    @property
    def proprietario(self):
        return self.__proprietario
        

coca_cola = Formulacocacola('Agua gaseficada', '5', '9', 'Asa Griggs Candler')
cria_senha = input('Digite a senha que deseja criar para acessar a Formula: ')

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\receita_secreta.pickle', 'wb') as arq:
    pickle.dump(coca_cola,arq)
    
senha = input('Digite a senha para acessar a formula secreta: ')
if senha == cria_senha:
    print('--------Acesso Permitido---------')
    with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos_CSV_Pickle_JSON\\receita_secreta.pickle', 'rb') as arq:
        coca_cola = pickle.load(arq)
        print(f'Ingrediente: {coca_cola.ingrediente}')
        print(f'Temperatura: {coca_cola.temperatura}°c')
        print(f'Açucar: {coca_cola.acucar} gramas')
        print(f'Proprietario: {coca_cola.proprietario}')
else:
    print('--------Acesso Negado---------')
    
    