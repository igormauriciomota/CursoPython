'''
Exercícios:

1 - Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome
como parâmetro. Estas classes devem herdar de outras duas chamadas
'Carnivoros' e 'Herbivoros', que possuem dois métodos cada ('caçar_animal' e
'comer_carne' para 'Carnivoros', 'procurar_arvore' e 'comer_folhas' para
'Herbivoros') e herdam de uma Superclasse chamada 'Animal', na qual possui
os métodos 'andar' e 'correr'. Por fim, instancie dois objetos, da classe 'Homem'
e da classe 'Urso', e execute todos os métodos.

Obs.: Crie um método para as classes 'Homem' e 'Urso' representando uma
ação característica de cada, por exemplo ler um livro para o homem e hibernar
para o urso.

'''

class Animal:
    
    def andar(self):
        print('Andando...')
        
    def correr(self):
        print('correndo...')
        
class Carnivoros(Animal):
    
    def cacar_animal(self):
        print('Caçando animal...')
        
    def comer_carne(self):
        print('Comendo carne...')
        
class Herbivoro(Animal):
    
    def procurar_arvor(self):
        print('Procurando arvore...')
        
    def comer_folha(self):
        print('Comendo folha...')

# Herda de Carnivoros e Herbivoros
class Homem(Carnivoros, Herbivoro):
    
    def __init__(self, nome):
        super().__init__()
        self.__nome = nome
        
    def nome(self):
        print(f'Nome: {self.__nome}')

    def lendo_livro(self):
        print('Lendo um Livro...')
        

class Urso(Carnivoros, Herbivoro):
    
    def __init__(self, nome):
        super().__init__()
        self.__nome = nome
        
    def nome(self):
        print(f'Nome: {self.__nome}')
        
    def hibernar(self):
        print('Hibernando...')
        

# Objeto
igor = Homem('Igor M')
igor.nome()
igor.lendo_livro()
igor.andar()
igor.procurar_arvor()
igor.correr()
igor.cacar_animal()
igor.comer_folha()
igor.comer_carne()
print('\n')
# Objeto
urso = Urso('Puffe')
urso.nome()
urso.hibernar()
urso.andar()
urso.procurar_arvor()
urso.correr()
urso.cacar_animal()
urso.comer_folha()
urso.comer_carne()