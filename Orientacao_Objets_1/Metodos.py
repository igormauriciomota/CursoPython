'''
Metodos: Programação Orientada a Objetos

o que é?

- São Funções dentro de uma classe

- Basicamente são divididos em  2 dois grupos

1 - Métodos de Instancia
2 - Métodos de Classes

(I) - Métodos de Instancia

- Tem esse nome porque precisa de uma instancia da classe para utilizar este método

- Método contrutor: E um método especial, conhecido tambem como 'método magico' (assim como outro que 
começam e terminam con dunder '__'). Possui esse nome pois constroi objetos da classe a que pertence;

Sintaxe: def __init__(self, parametros):

>> self: é o objeto/instancia. O nome self e convencional, pode-se ultilizar qualquer nome.   

Exemplo.: 1

class Carro:
    
    def __init__(self, portas, cor):
        # Atributos (Caracteristicas) do carro
        self.portas = portas # Público
        self.cor = cor # Público
        self.__arcondicionado = True # Privado
        
# Objeto        
carroPai = Carro(4, 'Prata')
print(type(carroPai)) # <class '__main__.Carro'>
print(carroPai.cor) # Prata
print(carroPai.__arcondicionado) # AttributeError:/Privado

----------------------------------------------------------------------------

Exemplo.: 2

class Sapato:
    
    qtdd = 7 # Atributo de classe
    
    def __init__(self, cor, tamanho, preco, qtddComprada):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.qtddComprada = qtddComprada
        # quantidade + Quantidade comprada
        Sapato.qtdd += self.qtddComprada
        
# Objeto Tamanco
tamanco = Sapato('Azul', 42, 1200, 2)
print(tamanco.qtdd) # 9
print(Sapato.qtdd) # 9


----------------------------------------------------------------------------

Exemplo.: 3

class Computador:
    # Metodo construtor usa o __init__
    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.poledadas = polegadas
        
    # Métodos instancia >> pcPrimo.memoria(1024, 8) <<
    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram
        
# Objeto        
pcPrimo = Computador('Preto', '1.5 kg', 20)

# Computador.memoria(1024, 8) # TypeError:
pcPrimo.memoria(1024, 8)
print(pcPrimo.hdd) # 1024


> Sempre evite criar métos que comecem e terminem com dunder. Pode haver conflitos com alguns métodos internos da linguagem

ex.: __name__ e __main__

> Nome de Métodos possuem APENAS letras ''minusculas'' Em caso de haver mais de uma palavra, separar por '_' underlene

ex.: controle_remoto, vasco_da_gama, igor_mota

----------------------------------------------------------------------------

(II) Métodos de Classes

Caracteristicas:

- Necessário utilizar o decorador: @classmethod

- Não há o 'self' mas sim o 'cls' que se refere a propria classee onde está o método

- 'cls' é tambem convencional

>> Sintaxe:

    @classmethod
    def nome_metodo(cls):

Exemplo.: 1 

# Método de classe não faz acesso a atributos de objeto instancia

class Computador:
    
    # Atributo de classes
    peixes = 98
    
    # Métodos de Classes
    @classmethod
    def conta_peixes(cls):
        print('Nome da classe: {cls}')
        print('Existem: {cls.peixes} peixes na classe: {cls}')  # Existem: {cls.peixes} peixes na classe: {cls}
        
    # Metodo construtor usa o __init__
    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.poledadas = polegadas
        
    # Métodos instancia >> pcPrimo.memoria(1024, 8) <<
    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram
        
# Objeto      
Computador.conta_peixes()
pcPrimo = Computador('Preto', '1.5 kg', 20)

# Computador.memoria(1024, 8) # TypeError:
pcPrimo.memoria(1024, 8)
print(pcPrimo.hdd) # 1024

----------------------------------------------------------------------------

(III) ____SUBTIPOS______

> construtor
> Públicos
> Privados
> Estáticos

----------------------------------------------------------------------------

->> Método Privado

Exemplo.: 1

class Computador:
    
    # Atributo de classes
    peixes = 98
    
    @classmethod
    def conta_peixes(cls):
        print('Nome da classe: {cls}')
        print('Existem: {cls.peixes} peixes na classe: {cls}')
        # Existem: {cls.peixes} peixes na classe: {cls}
        
    # Metodo construtor usa o __init__
    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.poledadas = polegadas
        
    # Métodos instancia >> pcPrimo.memoria(1024, 8) <<
    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram
        
    # Métodos Privados __nome
    def __caracteristicas(self):
        return f'{self.cor} e com {self.hdd} GB'
        
pcVovo = Computador('Dourado', 0.250, 21)
pcVovo.memoria(256, 2)

#print(pcVovo.__caracteristicas) # AttributeError:
#print(dir(Computador)

# Name Mangling -( _ + o nome da classe)
print(pcVovo._Computador__caracteristicas()) # Dourado e com 256 GB

>>  print(dir(Computador) mostra o que conseguimos fazer com nossa classe "Conputador"

['_Computador__caracteristicas', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'conta_peixes', 'memoria', 'peixes']

Exemplo.: 2

class Carro:
    
    def __init__(self, portas, cor):
        # Atributos (Caracteristicas) do carro
        self.portas = portas # Público
        self.cor = cor # Público
        self.__arcondicionado = True # Privado
        
# Objeto        
carroPai = Carro(4, 'Prata')
print(type(carroPai)) # <class '__main__.Carro'>
print(carroPai.cor) # Prata
print(carroPai._Carro__arcondicionado) # True

>> classe: _Carro

----------------------------------------------------------------------------

->> Método Estático

- Necessario utilizar o decorador: @staticmethod

- Sem parametros

class Computador:
    
    # Atributo de classes
    peixes = 98
    
    @classmethod
    def conta_peixes(cls):
        print('Nome da classe: {cls}')
        print('Existem: {cls.peixes} peixes na classe: {cls}')
        # Existem: {cls.peixes} peixes na classe: {cls}
        
    @staticmethod
    def modelo(): # Não possue parametros
        return 'HJEF348UG3HWFH'
        
    # Metodo construtor usa o __init__
    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.poledadas = polegadas
        
    # Métodos instancia >> pcPrimo.memoria(1024, 8) <<
    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram
        
    # Métodos Privados __nome
    def __caracteristicas(self):
        return f'{self.cor} e com {self.hdd} GB'

pcVovo = Computador('Azul', 0.500, 30)
pcVovo.memoria(256, 16)

print(Computador.modelo()) # Acessar tanto pela classe 
print(pcVovo.modelo()) # Acessar pelo Objeto

'''


class Computador:
    
    # Atributo de classes
    peixes = 98
    
    @classmethod
    def conta_peixes(cls):
        print('Nome da classe: {cls}')
        print('Existem: {cls.peixes} peixes na classe: {cls}')
        # Existem: {cls.peixes} peixes na classe: {cls}
        
    # Metodo construtor usa o __init__
    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.poledadas = polegadas
        
    # Métodos instancia >> pcPrimo.memoria(1024, 8) <<
    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram
        
    # Métodos Privados __nome
    def __caracteristicas(self):
        return f'{self.cor} e com {self.hdd} GB'
        
pcVovo = Computador('Dourado', 0.250, 21)
pcVovo.memoria(256, 2)
