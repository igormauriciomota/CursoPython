#class
#Syntaxe
# _____METODO ESTATICO_______
"""
#__init__(self): o init e chamado na programação de contrutor, 
# #permite criar a funcionalidae inicial de sua classe terá
class Computador:
    def __init__(self):
        self.marca = 'Asus'
        self.memoria_ram = '8gb'
        self.placa_de_vide = 'Nvidia'
    pass

# o (self): serve pra acessar a propriedade de uma instancia

# Precisamos instanciar a class criando variaveis
computador1 = Computador()
computador2 = Computador()
computador3 = Computador()
print(computador1.marca,computador1.memoria_ram,computador1.placa_de_vide)

"""
# _____METODO DINAMICO_______

#__init__(self): o init e chamado na programação de contrutor, 
# #permite criar a funcionalidae inicial de sua classe terá
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_vide = placa_de_video
    pass

# o (self): serve pra acessar a propriedade de uma instancia

# Precisamos instanciar a class criando variaveis
computador1 = Computador('Azus','8gb','Nvidia')
computador2 = Computador('Del','10gb','GeForce')
computador3 = Computador('Lenovo','16gb','ATM')
print(computador1.marca,computador1.memoria_ram,computador1.placa_de_vide)
print(computador2.marca,computador2.memoria_ram,computador2.placa_de_vide)
print(computador3.marca,computador3.memoria_ram,computador3.placa_de_vide)
