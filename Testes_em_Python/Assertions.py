'''
Assertions(Afirmações) 

- Assertions permite econtrar bugs rapidamente;
- Ele irá tetar se uma afirmação é verdadeira, caso sim, roda o código, se não retorna um erro.  
- Pode ser usado no meio dos códigos, sem perdas.  
- Usado para checar tipos de parametros, classes, valores,....   
- São usados mais como complemento dos unittests

NÂO é recomendado utilizar o assert como principal teste, pois pode ser desabilitado fcilmente com o (-O)
para utiliza-lo, basta escrever no terminal (python -O nome_do_arquivo)

Modo de declaração:
assert condição

Ex. 1 Da pra escrever uma mensagemde erro

#  Ele irá tetar se uma afirmação é verdadeira, caso sim, roda o código, se não retorna um erro. 
mensagem = 'Tamo junto'
assert mensagem == 'Tamojunto', 'Mensagem Incorreta'  # Retorna um erro chamado AssertionError: Mensagem Incorreta
print(mensagem)

Ex. 2

#  Ele irá tetar se uma afirmação é verdadeira, caso sim, roda o código, se não retorna um erro. 
mensagem = 'Tamo junto'
assert mensagem == 'Tamo junto', 'Mensagem Incorreta'
print(mensagem)

Ex. 3

numero = 10j
assert type(numero) is int, 'O numero não é inteiro'
print(numero)

EX. 4 -> Verificar se um Objeto faz parte de uma determinada classe

class Teste:
    
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        return self.__nome
    
maria = Teste('Maria')
assert isinstance(maria, Teste)
print(maria.nome)

Ex. 5

def apaga_arquivos(senha):
    senha_confirma = '123'
    assert senha == senha_confirma, 'Digite a senha correta'
    print('APAGUE TODOS OS SEUS ARQUIVOS')
    

apaga_arquivos(input('Digite a senha: '))

'''

def apaga_arquivos(senha):
    senha_confirma = '123'
    assert senha == senha_confirma, 'Digite a senha correta'
    print('APAGUE TODOS OS SEUS ARQUIVOS')
    

apaga_arquivos(input('Digite a senha: '))

    



