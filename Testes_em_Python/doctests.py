'''
Doctests:



Exemplo 1

from math import pi


def circulo(raio):
    """
    Calcula a área em cm² de um circulo
    raio: Raio em cm² do circulo
    >>> circulo(2)
    12.57
    """
    area = round(pi * (raio ** 2),2)
    return area

def retangulo(base,altura):
    """
    calcula a área em cm² de um retangulo
    >>> retangulo(2,2)
    4
    """
    area = base * altura
    return area


print(circulo(7))
print(retangulo(3,3))

>>> from doctests import circulo,retangulo

Para rodar o programa no terminal com maior riqueza de detalhes execute: python -m doctest -v nome_modulo.py

Exemplo 2

class Operacoes:
    
    
    def __init__(self,valor):
        self.__valor = valor
        
    @property
    def valor(self):
        return self.__valor
    
    def incrementa(self):
        """
        Aumenta em 1 o valor do objeto
        >>> numero = Operacoes(2)
        >>> numero.incrementa()
        1
        """
        self.__valor += 1
        return self.__valor
    
    def decrescimo(self):
        """
        Diminui em 1 o valor do objeto
        >>> numero = Operacoes(2)
        >>> numero.decrescimo()
        1
        """
        self.__valor -= 1
        return self.__valor
    
numero = Operacoes(4)
print(numero.valor)
print(numero.decrescimo())
print(numero.incrementa())
print(numero.incrementa())
print(numero.incrementa())

Exemplo 3 -> OBS:

def gritar(palavra):
    """
    Transforma a palavra em letras maiusculas
    >>> gritar('goollll')
    "GOOLLLL" # Usar aspas simples em docteste 'GOOLLLL'
    """
    return f"{palavra.upper()}"
    # Cuidado com o uso de aspas duplas ou simples em doctests

'''




