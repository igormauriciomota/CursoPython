"""
Ferramenta Uteis

1) Operadores Walrus( significa = Morsa):

- Permite realizar a declaração e retorno de velor em uma mesma linha
Ex: # print(x = 1) #Não é possivel de ser realizado, mas agora temos o operador walrus:

Como declarar?
- variavel := espressão/valor

Ex.1

print(x := 1)
print(x)

Ex.2 permite fazer uma declaração de uma variavel dentro da minha condicional;

fruta = 'Morango'

if fruta_preferida := input('Qual sua fruta favorita: ') == fruta:
    print('Voce e uma pessoa saudavel')
    
2) Operações Matematicas:

Ex. 1

- Bibiliotecas que são usadas

import math

# Imprimir o Radiano do angulo
angulo = 60
print(math.radians(angulo)) # 1.0471975511965976

Ex. 2

# Log de 2 na base 10
numero = 2
print(math.log10(numero)) # 0.3010299956639812

Ex.3 

# list comprehension

lista = [i for i in range(1,18)]

# produto de toda lista
print(math.prod(lista)) # 355687428096000

Ex. 4 

import statistics

# list comprehension

lista = [i for i in range(1,18)]

# Media
print(statistics.mean(lista)) # 9

Ex. 5 

import statistics

# list comprehension

lista = [i for i in range(1,18)]

# Variancia
print(statistics.variance(lista)) # 25.5

3) Type Hinting:

- Especificação de tipos Otimizada

def converte_str_to_int(numero: str) -> int:
    return int(numero)

print(converte_str_to_int('10'))

4) TexBlob:

- Realiza traduções com python

Bibilioteca
- pip install textblob

# 
from textblob import TextBlob

# Frase original
frase = "Olá, como você está?"

# Cria um objeto TextBlob
texto = TextBlob(frase)

# Traduzindo para o inglês
traducao_para_ingles = texto.translate(to='en')

print("Original:", frase)
print("Traduzido para inglês:", traducao_para_ingles)

"""






