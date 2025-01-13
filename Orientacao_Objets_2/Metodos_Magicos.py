'''
Métodos Magicos

- Métodos magicos são métodos que possuem dunder (__) em seus nomes;

Exemplos:

__init__ 
__repr__
__str__
__add__
__mul__
__len__
__del__

1 - Primeiro Metodo


'''

class Carro:
    
    def __init__(self, modelo, cor, portas, valor, ano):
        self.modelo = modelo
        self.cor = cor
        self.portas = portas
        self.valor = valor
        self.ano = ano
        
    def __repr__(self):
        return f'Carro {self.modelo}, {self.portas} portas e ano {self.ano}'
    
    # o __str__ tem preverencia de ordem
    def __str__(self):
        return f'Carro {self.cor} que vale {self.valor}'
    
    # concatena ou soma objetos
    def __add__(self, other):
        return f'{self}.....{other}'
    
    #
    def __mul__(self, other):
        if isinstance(other, int):
            result = ' '
            for i in range(other):
                result += ' ' + str(self)
            return result
        return 'E necessario um número inteiro para multiplicar'
    
    def __len__(self):
        return self.portas
    
    def __del__(self):
        print('Objeto do tipo carro deletado!')
    
        
carro1 = Carro('Fiat', 'Azul', 4, 60000, 2018)
carro2 = Carro('Audi', 'Preto', 2, 80000, 2021)

print(carro1)
print(carro2)    

print(carro1 + carro2) # __add__ Carro Azul que vale 60000.....Carro Preto que vale 80000
print(carro1 * 5)

print(len(carro1))
print(len(carro2))

