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
print(Jaguar)    # <__main__.Carro object at 0x0000016DBB355E20>    

# Por baixo dos panos o que acontece? Assim que passo Carro(), e como se a palavra init fosse substituida por Carro e Jaguar, passase
como primeiro atributo, Ficando assim: Jaguar = Carro(Jaguar)



'''

class Carro:
    
    def __init__(self): # Lembrando que o __init__ é o método contrutor que irá construir nosso objeto
        print(self) # <__main__.Carro object at 0x0000016DBB355E20> 
        
# Como criar Objeto: nome = classe(Parametro)
Jaguar = Carro()
print(Jaguar)    # <__main__.Carro object at 0x0000016DBB355E20>    
# Por baixo dos panos o que acontece?
