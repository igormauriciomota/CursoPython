'''
1) Aplique assert’s no código abaixo e descreva o que o programa faz:

'''

class ContaCorrente:
    
    def __init__(self, nome, num_conta, saldo=0.0):
        assert type(nome) is str, 'O nome deve ser string'
        assert type(num_conta) is int, 'O numero da conta deve ser inteiro'
        assert type(saldo) is float, 'O Salado deve ser float para realizar operações bancarias'
        assert saldo >= 0, 'O valor do saldo criado deve ser maior ou igual a zero'
        self.__nome = nome
        self.__num_conta = num_conta
        self.__saldo = saldo
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def num_conta(self):
        return self.__num_conta
    
    def deposito(self, valor):
        assert valor >= 0, 'O valor de saque deve ser positivo'
        assert type(valor) is float, 'O valor para deposito deve ser float para realizar operaçoes bancarias'
        self.__saldo = self.__saldo + valor
        
    def saque(self, valor):
        assert valor >= 0, 'O valor de saque deve ser positivo'
        assert type(valor) is float, 'O valor para deposito deve ser float para realizar operaçoes bancarias'
        assert self.__saldo >= valor, f'Dinheiro insuficiente, voce tem disponivel: R$ {self.__saldo} para saque'
        self.__saldo = self.__saldo - valor
        
pessoa = ContaCorrente('igor', 12345)
pessoa2 = ContaCorrente('Vanessa', 67891,500.0)

#pessoa2.saque(400.0)
assert isinstance(pessoa, ContaCorrente), 'Pessoa não encontrada no Banco de dados'
assert isinstance(pessoa2, ContaCorrente), 'Pessoa não encontrada no Banco de dados'




