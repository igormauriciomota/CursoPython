'''
Atributos e Objetos

Definição:

a) Atributo: São Caracteristicas do Objeto que a Classe irá controlar

Ex.: 

Classe Carro: tem como
Atributo: potencia, numero de bancos, velocidade maxima

b) Objeto: E justamente o objeto da vida real que sera controlado no programa..

Ex.:

Classe Carro: 
Objeto: Corolla, Civic, Porshe

Classe Animal: 
Objeto: tartaruga, cachorro, gato

--------------------------------------------------------------------------

(I) Objeto

Ex.: self é o objeto em si que voce criar

>> Como criar um objeto?

- nome = nome_da_classe(atributos que deseja)

class Carro:
    
    def __init__(self): # Lembrando que o __init__ é o método contrutor que irá construir nosso objeto
        print(self) # <__main__.Carro object at 0x0000016DBB355E20> 
        
# Como criar Objeto: nome = classe(Parametro)
Jaguar = Carro()
print(Jaguar)    # Ao imprimir jaguar aparecerá o endereço de memoria dele, que e o mesmo de self
<__main__.Carro object at 0x0000016DBB355E20>    

# Por baixo dos panos o que acontece? Assim que passo Carro(), e como se a palavra init fosse substituida por Carro e Jaguar, passase
como primeiro atributo, Ficando assim: Jaguar = Carro(Jaguar)

--------------------------------------------------------------------------
(II) Atributos

Existem tres tipos de Atributos:

1- Atributos de instancia
2- Atributos de Classe
3- Atributos de Dinamicos

-   ---------------------------------------------

1- Atributos de instancia:

>> São os atributos declarados dentro do metodo construtor -> (__init__(self)):

Ex:

class Carro:
# vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
# dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.vel_maxima = vel_maxima
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado

# Objeto: jaguar-> os tres atributos criados obrigatoriamente tem de ter tres 3 argumentos passados, 
# se nao for passado gerara TypeError     
jaguar = Carro(220, 1.6, 6)
print(f'A Potencia do Jaguar: {jaguar.potencia}')
print(f'A Veloxidade Maxima do Jaguar: {jaguar.vel_maxima}')
print(f'O Numero de Bnacos do Jaguar: {jaguar.num_banco}')

-   ---------------------------------------------

2- Atributos de Classe

>> São os atributos que são declarados diretamente na classe, fora de qualquer método

>> Caracteristicas: e justamente que esses atributos servem para todos os objetos declarados

>> A vantagem de usar atributos de classe é o menor uso de memoria. Pois requer apenas 1 espaço para todos os objetos

Ex.:

class Carro:
    # "atributo de classe"
    nitro = 1.1 # # Vamos aumentar a velocidade maxima de cada objeto em 10%
    
# vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
# dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa variavel agora utiliza: nome_classe.atributo/variavel criada
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado


# Objeto: 
Jaguar = Carro(250,350,5)
print(f'A Veloxidade Maxima do Jaguar: {Jaguar.vel_maxima}')
print(Jaguar.nitro) # O atributo de classe nitro e criado para todos os objetos
print(Carro.nitro) # nitro atributo de classe
print(Carro.potencia) # E um atributo de instancia, AttributeError

-   ---------------------------------------------

3- Atributos de Dinamicos

>> São os atributos que são criados ao longo da execução do programa, sendo que ele estará vinculado 
apenas ao objeto que o criou

Ex.: 1

class Carro:
    # "atributo de classe"
    nitro = 1.1 # # Vamos aumentar a velocidade maxima de cada objeto em 10%
    
    # vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
    # dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa variavel agora utiliza: nome_classe.atributo/variavel criada
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado
        

# Objeto: 
Jaguar = Carro(250,350,5)
# Atributo dinamico: fora da classe
Jaguar.preco = 300000
print(Jaguar.preco)

Ex.: 2

class Carro:
    # "atributo de classe"
    nitro = 1.1 # # Vamos aumentar a velocidade maxima de cada objeto em 10%
    
    # vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
    # dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa variavel agora utiliza: nome_classe.atributo/variavel criada
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado
        
    # Atributo dinamico: dentro da classe
    def cria_atributo(self):
        self.preco = 300000
        
# Objeto: 
Jaguar = Carro(250,350,5)
Jaguar.cria_atributo()
print(Jaguar.preco) # 300000

Ex.: 3

class Carro:
    # "atributo de classe"
    nitro = 1.1 # # Vamos aumentar a velocidade maxima de cada objeto em 10%
    
    # vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
    # dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa variavel agora utiliza: nome_classe.atributo/variavel criada
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado
        
    # Atributo dinamico: dentro da classe
    def cria_atributo(self):
        self.preco = 300000
        
# Objeto: 
Jaguar = Carro(250,350,5)
Porche = Carro(260,310,5)
Jaguar.cria_atributo()
print(Jaguar.preco) # 300000
print(Porche.preco) # AttributeError: pois o atributo dinamico pertence apenas ao objeto que o criou

-   ---------------------------------------------

# Complementação: DICAS

>> Como deletar atributos?

a) print(objeto.__dict__) # Retorna um dicionario com todos os atributos de instancia
b) del objeto.atributo de instancia # Deleta o atributo

Ex.:

class Carro:
    # "atributo de classe"
    nitro = 1.1 # # Vamos aumentar a velocidade maxima de cada objeto em 10%
    
    # vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
    # dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa variavel agora utiliza: nome_classe.atributo/variavel criada
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado
        
    # Atributo dinamico: dentro da classe
    def cria_atributo(self):
        self.preco = 300000
        
# Objeto: 
Jaguar = Carro(250,350,5)
Porche = Carro(260,310,5)
Jaguar.preco = 320350
print(Jaguar.__dict__) # Retorna um dicionario {'vel_maxima': 275.0, 'potencia': 350, 'num_banco': 5, 'estado': False}
del Jaguar.estado # Deleta o estado do objeto Jaguar {'vel_maxima': 275.0, 'potencia': 350, 'num_banco': 5}
del Jaguar.preco # Deleta tambem atributo dinamico
del Porche.potencia # Deleta a potencia do objeto Porche {'vel_maxima': 286.0, 'num_banco': 5, 'estado': False}
print(Jaguar.__dict__) # Retorna um dicionario {'vel_maxima': 275.0, 'potencia': 350, 'num_banco': 5, 'estado': False}
print(Porche.__dict__) # Retorna um dicionario {'vel_maxima': 286.0, 'potencia': 310, 'num_banco': 5, 'estado': False}

-   ---------------------------------------------

Subdivisão: Atributos Publicos X Privados

- Na teoria atributos publicos podem ser acessados por todos, enquanto privado não.  

Como declarar cada uma?

Ex: Declara um atributo Publico
self.vel_maxima
self.potencia

Ex: Declara um atributo Privado
self.__potencia 
self.__vel_maxima

Ex.:

class Carro:
    # "atributo de classe"
    nitro = 1.1 # # Vamos aumentar a velocidade maxima de cada objeto em 10%
    
    # vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
    # dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.__vel_maxima = vel_maxima * Carro.nitro # Para acessar essa variavel agora utiliza: nome_classe.atributo/variavel criada
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado
        
    # Atributo dinamico: dentro da classe
    def cria_atributo(self):
        self.preco = 300000
        
# Objeto: 
Jaguar = Carro(250,350,5)
Porche = Carro(260,310,5)
# print(Porche.__vel_maxima) # AttributeError: atributo Privado
# print(Porche.vel_maxima) # AttributeError: atributo Privado
print(Porche.potencia)
print(Porche._Carro__vel_maxima) # Percebe-se que o python apresenta erro, porem e possivel acessar com o Name Mangling:

print(Objeto._classe__atributo privado

-   ---------------------------------------------

Incrementando nosso Programa

class Carro:
    # "atributo de classe"
    nitro = 1.1 # # Vamos aumentar a velocidade maxima de cada objeto em 10%
    
    # vel_maxima, potencia, num_bancos: São os meus "atributos de instancia", pois estão sendo declarados 
    # dentro do meu metodo construtor
    def __init__(self, vel_maxima, potencia, num_bancos):
        # Pra armazenar estes atributos usamos self.atributo = atributo
        self.__vel_maxima = vel_maxima * Carro.nitro # Para acessar essa variavel agora utiliza: nome_classe.atributo/variavel criada
        self.potencia = potencia
        self.num_banco = num_bancos
        self.estado = False # Variavel estado irá representar se o carro está ligado ou desligado
        
    def liga_desliga(self):
        if self.estado == False:
            self.estado = True
        else:
            self.estado = False

        
# Objeto: 
Jaguar = Carro(250,350,5)
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)


'''


