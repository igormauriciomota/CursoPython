# _____METODO_______

#__init__(self): o init e chamado na programação de contrutor, 
# #permite criar a funcionalidae inicial de sua classe terá
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_vide = placa_de_video
        
    def Ligar(self):
        print('Estou ligado')
        
    def Desligado(self):
        print('Estou desligado')
    
    def ExibirInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_vide)


computador1 = Computador('Azus','8gb','Nvidia')
computador1.Ligar()
computador1.Desligado()
computador1.ExibirInformacoes()