'''
1) Crie uma Classe Pessoa que recebe no método construtor: nome, idade, cpf
e o tempo de trabalho como atributos de uma pessoa. Também, declare um
método chamado aposentadoria e outro com o nome de salario_aposentadoria,
ambos serão implementados pelas classes Filhas. Dica: Utilize os conceitos
aprendidos em polimorfismo.

Após isso, crie duas classes: Homem e Mulher, as duas sendo classes Filhas
de Pessoa. Dentro da classe Homem desenvolva o método aposentadoria que
irá testar se o objeto possui idade maior ou igual a 65 e um tempo de trabalho
maior ou igual a 15 anos, caso positivo, retorne ‘Você pode se aposentar’, caso
contrário ‘Ainda não atingiu os requisitos para se aposentar’. Também
implemente o método salario_aposentadoria que irá testar se o objeto possui
idade maior ou igual a 65 e um tempo de trabalho maior ou igual a 15 anos,
caso positivo, calcule e retorne o sálario de direito pela seguinte equação:
salário=1000+(tempode trabalho−15)∗200 Caso contrário, retorne ‘Você não pode se aposentar’. 

Faça o mesmo procedimento da classe Homem, para a classe Mulher, porém ao invés da
idade utilizada como comparação ser 65, faça com 60.
Utilize Doctests para fazer testes na classe Homem e Unittests na classe

Mulher. Utilize o método TDD.

'''

class Pessoa:
    
    def __init__(self, nome, idade, cpf, tempo_trabalho):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__tempo_trabalho = tempo_trabalho
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def tempo_trabalho(self):
        return self.__tempo_trabalho
    
    def aposentadoria(self):
        raise NotImplementedError('Metodo especifico de criterio para a SubClasse')
    
    def salario_aposentadoria(self):
        raise NotImplementedError('Metodo especifico de criterio para a SubClasse')
    
    
class Homem(Pessoa):
    
    def __init__(self, nome, idade, cpf, tempo_trabalho):
        super().__init__(nome, idade, cpf, tempo_trabalho)
    
    def aposentadoria(self):
        """
        Verifica se a pessoa pode se aposentar
        >>> maicon = Homem('Maicon',65,123456,20)
        >>> maicon.aposentadoria()
        'Voce pode se aposentar'
        
        >>> flavio = Homem('Flavio',61,123456,22)
        >>> flavio.aposentadoria()
        'Ainda não atingiu os requisitos para se aposentar'
        """
        if self.idade >= 65 and self.tempo_trabalho >= 15:
            return 'Voce pode se aposentar'
        return 'Ainda não atingiu os requisitos para se aposentar'
    
    def salario_aposentadoria(self):
        """
        Verifica quanto é o salario do aposentado
        
        >>> maicon = Homem('Maicon',65,123456,20)
        >>> maicon.salario_aposentadoria()
        2000

        >>> flavio = Homem('Flavio',61,123456,22)
        >>> flavio.salario_aposentadoria()      
        'Você não pode se aposentar'
        
        """
        if self.idade >= 65 and self.tempo_trabalho >= 15:
            salario = 1000 + (self.tempo_trabalho - 15) * 200
            return salario
        return 'Você não pode se aposentar'
    
    
    
class Mulher(Pessoa):
    
    def __init__(self, nome, idade, cpf, tempo_trabalho):
        super().__init__(nome, idade, cpf, tempo_trabalho)
    
    def aposentadoria(self):
        if self.idade >= 60 and self.tempo_trabalho >= 15:
            return 'Voce pode se aposentar'
        return 'Ainda não atingiu os requisitos para se aposentar'
    
    def salario_aposentadoria(self):
        if self.idade >= 60 and self.tempo_trabalho >= 15:
            salario = 1000 + (self.tempo_trabalho - 15) * 200
            return salario
        return 'Você não pode se aposentar'

# Objeto
nome = Pessoa('Maicon',65,123456,20)
nome = Pessoa('Flavia',59,123456,22)

