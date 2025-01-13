'''
POO Propriedades

- Métodos públicos utilizados para manipular atributos/metodos privados;

Exemplo:

class Celular:
    
    def __init__(self, data, senha, saldo, msg):
        self.__data = data
        self.__senha = senha
        self.__saldo = saldo
        self.__msg = msg
        
    # Propriedade São Decoradores
    @property    
    def data(self):
        return f'Data de hoje: {self.__data}'
    
    @property 
    def senha(self):
        return self.__senha
    
    @property 
    def saldo(self):
        return self.__saldo
    
    @property 
    def msg(self):
        return self.__msg
    
    # Decorador setter: é atribuir um valor ao campo correspondente/manipular valores de atributos privados
    @msg.setter
    def msg(self, resposta):
        self.__msg = resposta
    
    
# Objeto
cel1 = Celular('18/11/2024', 'Bananas123', 3210, 'Estamos te esperando!')
cel2 = Celular('10/03/2023', 'Xbaicon22', 4210, 'Sua entrega chega hoje!')

print(cel1.data) # Data de hoje: 18/11/2024
print(cel2.data) # Data de hoje: 10/03/2023

print(cel1.senha)
print(f'Saldo total: {cel1.saldo + cel2.saldo}') # Saldo total: 7420 

# cel1
print(cel1.msg)
cel1.msg = 'Passo ai hoje!' # Mode de alterar
print(cel1.msg)

# cel2
print(cel2.msg)
cel2.msg = 'Espero que sim!' # Mode de alterar
print(cel2.msg)



'''

class Celular:
    
    def __init__(self, data, senha, saldo, msg):
        self.__data = data
        self.__senha = senha
        self.__saldo = saldo
        self.__msg = msg
        
    # Propriedade São Decoradores
    @property    
    def data(self):
        return f'Data de hoje: {self.__data}'
    
    # Atributo
    @property 
    def senha(self):
        return self.__senha
    
    # Atributo
    @property 
    def saldo(self):
        return self.__saldo
    
    # Atributo
    @property 
    def msg(self):
        return self.__msg
    
    # Decorador setter: é atribuir um valor ao campo correspondente/manipular valores de atributos privados
    @msg.setter
    def msg(self, resposta):
        self.__msg = resposta
        
    # mensagem e um metodo/ que com tem dois atributos self.__data e self.__msg
    @property
    def mensagem(self):
        return f'Data: {self.__data}. Mensagem: {self.__msg}'
    
    
# Objeto
cel1 = Celular('18/11/2024', 'Bananas123', 3210, 'Estamos te esperando!')
cel2 = Celular('10/03/2023', 'Xbaicon22', 4210, 'Sua entrega chega hoje!')

print(cel1.data) # Data de hoje: 18/11/2024
print(cel2.data) # Data de hoje: 10/03/2023

print(cel1.senha)
print(f'Saldo total: {cel1.saldo + cel2.saldo}') # Saldo total: 7420 

# cel1
print(cel1.msg)
cel1.msg = 'Passo ai hoje!' # Mode de alterar
print(cel1.msg)

# cel2
print(cel2.msg)
cel2.msg = 'Espero que sim!' # Mode de alterar
print(cel2.msg)

print(cel1.mensagem)
print(cel2.mensagem)

