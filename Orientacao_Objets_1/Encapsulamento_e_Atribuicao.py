'''
Programação Orientada a Objetos Encapsulamento e Abstração

>> Encapsulamento: Em POO ocorre o encapsulamento do codigo dentro das classes, promovendo mais segurança ao 
sistema e limitando o acesso de objetos a determinados atributos. O agrupamento de métodos e atributos como o encapsulamento
é possivel a realização da abstração;

>> Abstração: Disponibilização ao usuario somente de métodos e atributos realmente necessrio de ser apresentado,
Métodos e atributos privados permanecem ocultos. usuario pode somente editar;

(I) Metodo Publico: Exemplo Jogador tem acesso a todos os valores, isso nao e correto, ele pode alterar todos os atributos

class Jogo:
    
    nivel = 8
    
    def __init__(self, forca, magia, resistencia):
        self.forca = forca
        self.magia = magia
        self.resistencia = resistencia
        self.nivel = Jogo.nivel
        
    def atacar_raio(self):
        self.resistencia -= 5
        self.magia -= 10
        
    def atacar_soco(self):
        self.resistencia -= 10
        self.forca -= 10
        
    def pular_nivel(self):
        Jogo.nivel += 1
        self.nivel = Jogo.nivel
        
    def status(self):
        print(f'Força: {self.forca} Magia: {self.magia} Resistencia: {self.resistencia} Nível: {self.nivel}')
        # Força: 76 Magia: 95 Resistencia: 88 Nível: 8
        
player1 = Jogo(76, 95, 88)
player1.status()

player1.atacar_raio()
player1.status()

player1.atacar_soco()
player1.status()

player1.pular_nivel()
player1.status()

print(player1.forca)
print(player1.magia)
print(player1.resistencia)
print(player1.nivel)

player1.forca = 100000
player1.magia = 100000
player1.resistencia = 100000
player1.nivel = 99
player1.status()

Força: 76 Magia: 95 Resistencia: 88 Nível: 8
Força: 76 Magia: 85 Resistencia: 83 Nível: 8
Força: 66 Magia: 85 Resistencia: 73 Nível: 8
Força: 66 Magia: 85 Resistencia: 73 Nível: 9
66
85
73
9
Força: 100000 Magia: 100000 Resistencia: 100000 Nível: 99

(II) Metodo Privado: Utilizando a abstração

class Jogo:
    
    nivel = 8
    
    def __init__(self, forca, magia, resistencia):
        self.__forca = forca
        self.__magia = magia
        self.__resistencia = resistencia
        self.__nivel = Jogo.nivel
        
    def atacar_raio(self):
        self.__resistencia -= 5
        self.__magia -= 10
        
    def atacar_soco(self):
        self.__resistencia -= 10
        self.__forca -= 10
        
    def __pular_nivel(self):
        Jogo.nivel += 1
        self.__nivel = Jogo.nivel
        
    def status(self):
        print(f'Força: {self.__forca} Magia: {self.__magia} Resistencia: {self.__resistencia} Nível: {self.__nivel}')
        # Força: 76 Magia: 95 Resistencia: 88 Nível: 8
        
player1 = Jogo(76, 95, 88)
player1.status()

player1.atacar_raio()
player1.status()

player1.atacar_soco()
player1.status()


'''

