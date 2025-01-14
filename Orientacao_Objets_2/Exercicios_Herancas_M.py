'''
1 - Desenvolva o sistema de um controle universal para uma casa. O controle deve
ser a Classe-Mãe, que contém o método liga/desliga e é herdada por outras três
classes (equipamentos controlados): ar-condicionado, micro-ondas e televisão, que
controlam, respectivamente, temperatura, tempo e volume em métodos dentro das
classes. Além disso, os métodos construtores das Classes Filhas recebem a variável
controlada em seu valor atual, por exemplo 'temperaturaAtual'.
Obs.: Utilize também propriedades para realizar o acesso aos atributos.

'''

class Controle:
    
    ligado = False
    def liga_desliga(self):
        self.ligado = not self.ligado
        

class Arcondicionado(Controle):
    
    def __init__(self, temperaturaAtual):
        super().__init__()
        self.__tempreraturaAtual = temperaturaAtual
        
    def controle_temperatura(self, temperatura):
        self.__tempreraturaAtual = temperatura
        
    @property
    def temperaturaAtual(self):
        return f'Temperatura atual: {self.__tempreraturaAtual}'
    

class Microondas(Controle):
    
    def __init__(self, tempoAtual):
        super().__init__()
        self.__tempoAtual = tempoAtual
        
    def controle_tempo(self, tempo):
        self.__tempoAtual = tempo
        
    @property
    def tempoAtual(self):
        return f'Tempo atual: {self.__tempoAtual}'


class Televisao(Controle):
    
    def __init__(self, volumeAtual):
        super().__init__()
        self.__volumeAtual = volumeAtual
        
    def controle_volume(self, volume):
        self.__volumeAtual = volume
        
    @property
    def volumeAtual(self):
        return f'Volume atual: {self.__volumeAtual}'
    
    
# Objeto
arc = Arcondicionado(45)
mic = Microondas(60)
tv = Televisao(85)

print(arc.ligado)
arc.liga_desliga()
print(arc.ligado)
print(arc.temperaturaAtual)
arc.controle_temperatura(35)
print(arc.temperaturaAtual)

