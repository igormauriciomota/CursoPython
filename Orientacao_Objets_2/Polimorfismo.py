'''
Polimorfismo:

- Significa muitaa formas (poli - muitas; morfis - formas)

- Por exemplo, um overriding é um representação de polimorfismo

(I) Exemplo com error:

class Comida:
    
    def __init__(self, alimento):
        self.__alimento = alimento
        
    @property
    def alimento(self):
        return self.__alimento
        
    def apresentar(self):
        raise NotImplementedError('Esse método só funciona se a sub classe implementa-lo sobrescreve-lo')
    
    
class Fruta(Comida):
    
    def __init__(self, alimento):
        super().__init__(alimento)
        
    def apresentar(self):
        print(f'Sou uma fruta, voce gosta de {self.alimento}')
        
class Carne(Comida):
    
    def __init__(self, alimento):
        super().__init__(alimento)


        
# Objeto
fruta = Fruta('Laranja')
fruta.apresentar() 

carne = Carne('Frango')
carne.apresentar()

(II) Correto tem de ter 

class Comida:
    
    def __init__(self, alimento):
        self.__alimento = alimento
        
    @property
    def alimento(self):
        return self.__alimento
    
    # Tem de sobrescrever o Metodo apresentar tambem nas classes filhas
    def apresentar(self):
        raise NotImplementedError('Esse método só funciona se a sub classe implementa-lo sobrescreve-lo')
    
    
class Fruta(Comida):
    
    def __init__(self, alimento):
        super().__init__(alimento)
        
    # o Metodo apresentar tem d estar em fruta
    def apresentar(self):
        print(f'Sou uma fruta, voce gosta de {self.alimento}')
        
class Carne(Comida):
    
    def __init__(self, alimento):
        super().__init__(alimento)
    
    # o Metodo apresentar tem de estar em carne
    def apresentar(self):
        print(f'Sou uma Carne, voce gosta de {self.alimento}')


        
# Objeto
fruta = Fruta('Laranja')
fruta.apresentar() 

carne = Carne('Frango')
carne.apresentar()

'''

class Comida:
    
    def __init__(self, alimento):
        self.__alimento = alimento
        
    @property
    def alimento(self):
        return self.__alimento
        
    def apresentar(self):
        raise NotImplementedError('Esse método só funciona se a sub classe implementa-lo sobrescreve-lo')
    
    
class Fruta(Comida):
    
    def __init__(self, alimento):
        super().__init__(alimento)
        
    def apresentar(self):
        print(f'Sou uma fruta, voce gosta de {self.alimento}')
        
class Carne(Comida):
    
    def __init__(self, alimento):
        super().__init__(alimento)
        
    def apresentar(self):
        print(f'Sou uma Carne, voce gosta de {self.alimento}')


        
# Objeto
fruta = Fruta('Laranja')
fruta.apresentar() 

carne = Carne('Frango')
carne.apresentar()

