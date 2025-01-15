'''
Herança Mútipla

- Uma classe pode herdar mútiplas classes ao mesmo tempo

- Existem dois tipos de herança multiplas: Direta e Indireta

- Independente do tipo, a sub classe herda todos os métodos e atributos da super classes

(I) Herança Multipla Direta;



class Energia:
    
    def __init__(self, ligado):
        self.__ligado = ligado
        
    @property
    def ligado(self):
        return self.__ligado
    
    def botao(self):
        self.__ligado = not self.__ligado
        
        
class Memoria:
    
    def __init__(self, ram):
        self.__ram = ram
        
    @property
    def ram(self):
        return self.__ram
    
    
class Monitor:
    
    def __init__(self, polegadas):
        self.__polegadas = polegadas
        
    @property
    def polegadas(self):
        return self.__polegadas
        
# Herança Multipla Direta;
class Computador(Energia, Memoria, Monitor):
    
    def __init__(self, ligado, ram, polegadas, valor):
        Energia.__init__(self, ligado)
        Memoria.__init__(self, ram)
        Monitor.__init__(self, polegadas)
        self.__valor = valor
        
    @property
    def valor(self):
        return self.__valor
    
    
# Objeto
meuPC = Computador(True, 8, 15.6, 3200)
print(meuPC.ram)
print(meuPC.polegadas)
print(meuPC.valor)
print(meuPC.ligado)
meuPC.botao()
print(meuPC.ligado)

(II) Herança Múltipla indireta



'''


class Energia:
    
    def __init__(self, ligado):
        self.__ligado = ligado
        
    @property
    def ligado(self):
        return self.__ligado
    
    def botao(self):
        self.__ligado = not self.__ligado
        
        
class Memoria(Energia):
    
    def __init__(self,ligado, ram):
        super().__init__(ligado)
        self.__ram = ram
        
    @property
    def ram(self):
        return self.__ram
    
class Monitor(Memoria):
    
    def __init__(self, ligado, ram, polegadas):
        super().__init__(ligado, ram)
        self.__polegadas = polegadas
        
    @property
    def polegadas(self):
        return self.__polegadas
        
# Herança Multipla Indireta;
class Computador(Monitor):
    
    def __init__(self, ligado, ram, polegadas, valor):
        super().__init__(ligado, ram, polegadas)
        self.__valor = valor
        
    @property
    def valor(self):
        return self.__valor
    
    
# Objeto
meuPC = Computador(True, 8, 15.6, 3200)
print(meuPC.ram)
print(meuPC.polegadas)
print(meuPC.valor)
print(meuPC.ligado)
meuPC.botao()
print(meuPC.ligado)

