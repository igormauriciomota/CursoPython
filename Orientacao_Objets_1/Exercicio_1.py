'''
Exercícios:

1) Crie uma classe chamada Personagem que irá receber como construtor o
nome completo, altura, peso e resistência (0-100) do personagem, além disso,
também crie um método que se chame poder que conterá todos os atributos de
instancia como privado não sendo possível alterá-los, sendo estes: magia,
persuasão, agilidade e forca, cada um avaliada de 0 a 100, por fim, retorne
apenas a soma de todos os pontos fornecidos. Crie 3 objetos personagens e
imprima o nome completo e quantidade de poder total do mais forte.

'''

class Personagem:
    
    def __init__(self, nome_completo, altura, peso, resistencia):
        self.nome_completo = nome_completo
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia
        
    def poder(self, magia, persuasao, agilidade, forca):
        self.__magia = magia
        self.__persuasao = persuasao
        self.__agilidade = agilidade
        self.__forca = forca
        return magia + persuasao + agilidade + forca
        
# Dicionario        
dict_poder = {}
        
thanos = Personagem('Thanos', 2, 120, 96)
dict_poder[thanos.nome_completo] = thanos.poder(50, 90, 78, 99)

thor = Personagem('Thor', 1.9, 90, 92)
dict_poder[thor.nome_completo] = thor.poder(65, 75, 82, 96)

hulck = Personagem('Hulck', 2.1, 200, 98)  
dict_poder[hulck.nome_completo] = hulck.poder(30, 61, 68, 97)      

# print(thanos.__dict__) # Retorna um dicionario com todos os atributos de cada objeto

maior = 0
nome = ''

for chave, valor in dict_poder.items():
    if maior < valor:
        maior = valor
        nome = chave
        
print(f'O mais forte: {nome} com {maior} ponto de poder')

