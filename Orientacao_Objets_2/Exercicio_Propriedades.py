'''
Exercícios:

1 - Crie uma classe contendo atributos públicos e privados representando
objetos pessoais. Após isso, crie uma propriedade pra cada atributo privado.
Instancie um objeto e faça acesso a todos os atributos. Utilize também o setter,
para alterar algum valor do objeto.

'''

class Objeto:
    
    def __init__(self, videogame, senhacelular, dinheiro, camisa, livro):
        self.__videogame =videogame
        self.__senhacelular = senhacelular
        self.__dinheiro = dinheiro
        self.camisa = camisa
        self.livro = livro
        
    @property
    def videogame(self):
        return self.__videogame
    
    @property
    def senhacelular(self):
        return self.__senhacelular
    
    @property
    def dinheiro(self):
        return self.__dinheiro
    
    @dinheiro.setter
    def dinheiro(self, quantidade):
        self.__dinheiro = quantidade
        
# Objeto        
joao = Objeto('Playstation', 'joaozinho007', 135, 'adidas', 'Cálculo 1')
maria = Objeto('Xbox360', 'floremel', 800, 'Gucci', 'Ingles em 1 hora')

print(joao.videogame)
print(joao.senhacelular)
print(joao.dinheiro)
joao.dinheiro = 5000
print(joao.dinheiro)
print(joao.camisa)
print(joao.livro)

print('\n')

print(maria.videogame)
print(maria.senhacelular)
print(maria.dinheiro)
maria.dinheiro = 14000
print(maria.dinheiro)
print(maria.camisa)
print(maria.livro)

