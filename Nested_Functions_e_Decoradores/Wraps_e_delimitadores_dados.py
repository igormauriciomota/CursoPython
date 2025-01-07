'''
Wraps e Forçando dados em decoradores

(I)

def tipo_dado(*tipo):
    def decorando(funcao):
        def convertendo_dados(*args, **kwargs):
        # Como args é imutavel devo criar um novo para alterar o tipo das variaveis
            altera_tipo = []
            altera_tipo.append(tipo[0](args[0]))
            altera_tipo.append(tipo[1](args[1]))
            return funcao(*altera_tipo,**kwargs)
        return convertendo_dados
    return decorando

@tipo_dado(complex, float)
def imprimindo(num1,num2):
    print(f'Numero complexo: {num1} e float: {num2}')
    
imprimindo('2', 2.5) # Numero complexo: (2+0j) e float: 2.5

--------------------------------------------------------------------------------

len() -  retorna o número de elementos (comprimento) em um iterador/objeto passado para a função . 
A função Python len() é usada para retornar um valor numérico que denota o comprimento da lista, 
tupla, string, array, dicionário, etc. fornecidos.

--------------------------------------------------------------------------------

(II) wraps:

- O que faz?

Copia os metadados da função antes de ser decorada para sua versão decorada. Portanto, utiliza um decorador não tira
a identidade da sua função;

- O que são metadados?

São dados sobre outros dados Ex: Decorador que é um dado que voce manipula em cima de outro dado(função decoradora).  

(III)

Explicando o problema:

def aprovados(funcao):
    """
    Essa função retorna uma lista completa do nome dos alunos aprovados
    """
    def decorador(*args, **kwargs):
        aprovado = []
        for chave,nota in kwargs.items():
            if nota >= 6:
                aprovado.append(chave)
        print(aprovado)
        return funcao(*aprovado)
    return decorador

@aprovados
def cont_alunos_aprovados(*args, **kwargs):
    """
    Apresenta a quantidade de alunos aprovcados
    """
    print(len(args))
    
cont_alunos_aprovados(Leticia=7,Joao=5,Maia=6,Cartos=8)

(IV)

Nos já vimos o __name__, ele retorna o nome da função a ser usada, enquanto o __doc__, retorna justamente a documentação
daquela função;

def aprovados(funcao):
    """
    Essa função retorna uma lista completa do nome dos alunos aprovados
    """
    def decorador(*args, **kwargs):
        """
        Função que decora e faz os testes de notas
        """
        print(f'{aprovados.__name__}') # Retornar o nome da função
        print(f'{aprovados.__doc__}') # Retorna a documentação de aprovados
        aprovado = []
        for chave,nota in kwargs.items():
            if nota >= 6:
                aprovado.append(chave)
        print(aprovado)
        return funcao(*aprovado)
    return decorador

@aprovados
def cont_alunos_aprovados(*args, **kwargs):
    """
    Apresenta a quantidade de alunos aprovcados
    """
    print(f'{cont_alunos_aprovados.__name__}') # Retorna o 'decorador'
    print(f'{cont_alunos_aprovados.__doc__}') # Retorna o doc. de decorador
    print(len(args))
    
cont_alunos_aprovados(Leticia=7,Joao=5,Maia=6,Cartos=8)


(V) >> Percebemos que ao imprimir a documantação de cont_alunos_ap´rovados, ele reconhece como a função decorador
isso é um problema, pois caso voce tenha um programa e queira consultar a documentação das funçoes profissionalmente,
pode ocorrer conflitos, pois seus metadados estão sobrepostos. 

-> Para consertar esse problema, utilizamos o >>'wraps'<<

from functools import wraps

def aprovados(funcao):
    """
    Essa função retorna uma lista completa do nome dos alunos aprovados
    """
    @wraps(funcao)
    def decorador(*args, **kwargs):
        """
        Função que decora e faz os testes de notas
        """
        print(f'{aprovados.__name__}') # Retornar o nome da função
        print(f'{aprovados.__doc__}') # Retorna a documentação de aprovados
        aprovado = []
        for chave,nota in kwargs.items():
            if nota >= 6:
                aprovado.append(chave)
        print(aprovado)
        return funcao(*aprovado)
    return decorador

@aprovados
def cont_alunos_aprovados(*args, **kwargs):
    """
    Apresenta a quantidade de alunos aprovcados
    """
    print(f'{cont_alunos_aprovados.__name__}') # Retorna o 'decorador'
    print(f'{cont_alunos_aprovados.__doc__}') # Retorna o doc. de decorador
    print(len(args))
    
cont_alunos_aprovados(Leticia=7,Joao=5,Maia=6,Cartos=8)

'''

