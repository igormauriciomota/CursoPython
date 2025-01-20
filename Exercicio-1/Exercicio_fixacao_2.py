'''
-----EXERCICIO-FIXAÇÃO-----

N-1 Crie uma classe Carro com propriedades como marca e modelo e um método para exibir essas informações.

# Atributos publicos
class Carro:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_infor(self):
        print(f'Carro: {self.marca} modelo {self.modelo}')
        
# Objeto        
carro = Carro('Toyota', 'Corolla')
carro.exibir_infor()

------------------------------

N-2 Modifique a classe Carro para usar encapsulamento nas propriedades.

# Atributos privados
class Carro:
    
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def exibir_infor(self):
        print(f'Carro: {self.__marca} modelo {self.__modelo}')
        
# Objeto        
carro = Carro('Toyota', 'Corolla')
carro.exibir_infor()

------------------------------

N-3 Crie uma classe Retangulo que calcule a área e o perímetro com base em suas dimensões.

class Retangulo:
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calculo_area(self):
        return self.largura * self.altura
    
    def calculo_perimetro(self):
        return 2 * (self.largura + self.altura)
    
#Objeto
ret = Retangulo(4,5)
print('Area: ', ret.calculo_area())

-------------------------------

N-4 Crie um método estático para converter uma temperatura de Celsius para Fahrenheit.

class Conversor:
    
    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
print('Temperatura em Fahrenheit: ', Conversor.celsius_para_fahrenheit(25))

-------------------------------

N-5 Implemente o método especial __str__ para exibir informações de forma legível.

class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        return f'Produto: {self.nome}, Preço: R$ {self.preco:.2f}'
    
# Objeto
produto = Produto('Notebook', 3500.00)
print(produto)

-------------------------------

N-6
'''


class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        return f'Produto: {self.nome}, Preço: R$ {self.preco:.2f}'
    
# Objeto
produto = Produto('Notebook', 3500.00)
print(produto)

