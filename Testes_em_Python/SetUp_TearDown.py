'''
Testes em Python Aplicando setUp e tearDown

-> São métodos que permitem a definição de comandos antes(setUp) e depois (tearDown) dos testes em si
-> Se o método setUp for sucedido, o médodo tearDow será executado, independente do resultado do método de teste
-> O setUp é muito usado para criar objetos e declarar variaveis
-> O tearDown faz a limpeza do sistema e o finaliza
-> O setUp e tearDown são executados uma vez a cada método de teste


Exemplo


'''

class BolsaDeValores:
    
    def __init__(self, nome, cpf, saldo=0):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def saldo(self):
        return self.__saldo

    def deposito(self, novo_dinheiro):
        if novo_dinheiro > 0:
            self.__saldo += novo_dinheiro
        else:
            return 'O valor de depósito deve ser positivo'
    
    def compra_acao(self,nome):
        acoes = {'Petrobras':30, 'Vale':80,'Weg':35,'Itau':32}
        for acao in acoes:
            if acao == nome:
                if self.__saldo >= acoes[acao]:
                    self.__saldo -= acoes[acao]
                else:
                    return 'Dinheiro insuficiente para compra, vá para o mercado fracionário' 
    
