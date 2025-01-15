
'''
Herança em Python

- Aumentar o alcance de nossas classes utilizando menos código;

- Se uma classe herda de outra classe, ela passa a herdar todos os atributos e métodos da classe herdada;

- A classe herdada é conhecida como:

- classe Mãe
- classe Pai
- classe Base
- classe Genérica
- Super classe 

- A classe que herda é conhecida como:

- classe Filha
- classe Especifica
- sub classe

'''
# Método super() pode acessar qualquer atributo0 é metodo da super classe
# Super classe
class Aparelho:
    
    def __init__(self, marca, peso, volume):
        self.__marca = marca
        self.__peso = peso
        self.__volume = volume
        
    def volume(self):
        return f'O volume está em {self.__volume}'
    
    def marca(self):
        return f'A marca do aparelho é {self.__marca}'
    
    def peso(self):
        return f'O peso do aparelho é {self.__peso}'
    
# Televisao e sub classe que herda Aparelho 
class Televisao(Aparelho):
    
    def __init__(self, marca, peso, volume, polegadas):
        super().__init__(marca, peso, volume)
        self.__polegadas = polegadas
        
    def polegadas(self):
        return f'A polegada da televisão e de {self.__polegadas}'

# Radio e sub classe que herda Aparelho        
class Radio(Aparelho):
    
    def __init__(self, marca, peso, volume, frequencia):
        super().__init__(marca, peso, volume)
        self.__frequencia = frequencia
        
    def frequencia(self):
        return f'A frequencia do radio e {self.__frequencia}'
    
    

tv = Televisao('LG', 2.5, 80, 52)
radio = Radio('Sony', 1, 75, 105)

print(tv.volume()) # O volume está em 80
print(radio.volume()) # O volume está em 75
print(tv.polegadas())

