'''
Programação Orientada a Objetos exercicio de seção parte 2

1 - Crie uma SuperClasse chamada 'Pessoa' que recebe como atributos nome,
cpf e salário. Após isso, construa a Classe Filha: 'Funcionario', que possui o
método sem parâmetros chamado 'promocao', que apenas acrescenta 10% no
salário a algum funcionário. Por sua vez, a classe 'Funcionario' deve ser
Classe Mãe de outras duas classes: 'Gerente' e 'Estagiario', e ambos precisam
ter o atributo 'codigo' em seu método construtor. Além disso, o gerente precisa
do atributo 'numEstagiarios', representando a quantidade de funcionário que
ele é responsável. Ainda, na classe gerente deve haver um método que
possibilite a alteração do código dos estagiários, sendo que os estagiários não
têm acesso a troca de codigo. Instancie 3 estagiários e 1 gerente. Dê
promoção para os dois primeiros estagiários e para o gerente.

Obs.: Utilize também um método mágico para representar as classes
'Estagiário' e 'Gerente', e propriedades para acessar os atributos de 'Pessoa'.

'''

class Pessoa:
    
    def __init__(self, nome, cpf, salario,):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, aumento):
        self.__salario = aumento
        
class Funcionario(Pessoa):
    
    def promocao(self):
        self.salario *= 1.1
        
class Gerente(Funcionario):
    
    def __init__(self, nome, cpf, salario, codigo, numEstagiario, codEstagiario):
        super().__init__(nome, cpf, salario)    
        self.__codigo = codigo
        self.__numEstagiario = numEstagiario
        self.__codEstagiario = codEstagiario
        
    def trocar_codigo(self, novoCodigo):
        self.__codEstagiario = novoCodigo
        
    def __repr__(self):
        return f'Sou o(a) Gerente {self.nome}, recebo {round(self.salario)} reais e quero um café'
    
class Estagiario(Funcionario):
    
        def __init__(self, nome, cpf, salario, codigo):
            super().__init__(nome, cpf, salario)
            self.__codigo = codigo
        
        def __repr__(self):
            return f'Sou o(a) Estagiario(a) {self.nome}, recebo {round(self.salario)} reais e tenho que levar um café ali na administração'
        
        
# Objeto
gerente = Gerente('Pablo', 12345678901, 12000, 'gege123', 3, 'es1234')
estagiario1 = Estagiario('Igor', 6845222682,1500,'es1234')
estagiario2 = Estagiario('Julia',5897079895,1500,'es1235')
estagiario3 = Estagiario('Carla',4597079896,1500,'es1236')

print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())
print(estagiario3.__repr__())
print('\n')

estagiario1.promocao()
estagiario2.promocao()
gerente.promocao()

print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())
print(estagiario3.__repr__())
