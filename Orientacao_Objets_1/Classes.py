'''
Classes

O que são? 

- conjunto de métodos e atributos que constroem o objeto

Ex.: Poderiamos criar uma Classe chamada controle que controla
->> Objeto: Ar condicionado
->> Atributo: Nivel de temperatura, liga/desliga, entre outros

>> Como declaro a classe?

class nome_definido:
    # Processo: tera os metodos e atributos

class Controle:
    pass # ultilizada para apenas passar a classe/função

(I) Regras de nomelatura de classes: 3 regras

1 - Palavras compostas devem ser separadas por letras maiusculas(SEM UNDERLINE) ex: ControleRobo
2 - A primeira letra deve sempre ser maiuscula ex: Tabela, Uva
3 - Sem acentos, caracteres especiais, dentre outros

Obs.: Por convenção utiliza as regras, pois as classes embutidas na linguagem Python como ex: print(type(10)) <cass 'int'>
tem sempre letras minusculas, por isso, e interessante diferenciar nossas proprias classes com letras MAIUSCULAS.  

Por que criar uma classe?

- Para criar novos tipos de dados

Exemplo 01:

class Animal:
    pass # ultilizada para apenas passar a classe/função

leao = Animal()
macaco = Animal()
print(type(leao)) # <class '__main__.Animal'>

Exemplo 02:

print(help(set)) >> help: Retorna a propria class

class set(object)
|  set() -> new empty set object
|  set(iterable) -> new set object
|
|  Build an unordered collection of unique elements.
|
|  Methods defined here:
|
|  __and__(self, value, /)
|      Return self&value.
|
|  __contains__(...)
|      x.__contains__(y) <==> y in x.
|
|  __eq__(self, value, /)

Metodos e Atributos de set: print(dir(set)) >> dir: Retorn os métodos e atributos da classe

['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
'__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', 
'__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
'__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', 
'__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

'''



