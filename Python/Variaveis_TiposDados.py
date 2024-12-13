
"""
Variaveis e Tipos de Dados
"""

"""
O Que são Variaveis?
    - São um modo de rotular ou nomear todos os dados pertencentes ao seu programa.
O Que são Dados?
    - São todas as informções que serão utilizadas ao longo do seu código. Podendo ser 
        números, palavras, frases, textos, dentre outros.
        
        
(I) Existem 2 tipos de Variaceis:

1) Variaveis Global: São variaveis que podem ser manipuladas ao longo de todo código.
2) Variaveis Local: São variaveis que podem ser manipuladas apenas em uma determinada parte do programa.

Como declarar variaveis?
nome = dados

È necessario algumas regras para nomear suas variaveis:
a) Em nome compostos devemos separar por underline (_) ou letras Maiusculas
Ex:
 - Modo certo: (Pythonico):
idadeJoao = 17
idade_joao = 17
IDADE_JOAO = 17
 - Modo errado: 
 idadejoao = 17 - ERRADO - tudo em letra minuscula
 
 b) Variaveis não devem possuir nenhum tipo de caracter especial (.,@,%,acentos,ç,entre outros)
 
 c) Variaveis não devem possuir apenas numeros em seu nome.
 Ex. 
 Modo errado:
 123 = 17 # ira acusar erro
 Modo certo:
 a123 = 17 #Letra no inicio e numero no final almenos uma letra.
 
 (II) Tipos de Dados:
    
    Obs: Para saber o tipo da variavel digite: type(variavel)
    a) Inteiros: Número que não possui casas decimais.
    
    Ex:
    idadeJoao = 17
    print(idadeJoao)
    print(type(idadeJoao))

    b) Flutuantes (float): Números que possuem casas decimais.
    - float utilisa se (.) ponto para separar os numeros e nao usa espaço em volta do ponto.
    - float mais riqueza de dados
    Ex:
    
    preco_banana = 5.59
    print(preco_banana)
    print(type(preco_banana))
    
    c) Complexo: numeros ex: 1 + 2j
    - Se um dado possuir a letra J e um numero complexo, tem de ser numeros
    
    Ex:
    numeroComplexo = 2 - 2j
    print(numeroComplexo)
    print(type(numeroComplexo))
    
    d) Booleana:
    - O valor 1 represemnta True (Verdadeiro) T letra maiuscula o resto minuscula.
    - O valor 2 representa False (Falso)
    
    Ex:
    
    e) String:
    - Todos os dados que estão entre aspas simples, aspas duplas ou aspas simples triplas.
    
    Ex:
    var_string = 'Tom cruise'
    print(var_string)
    print(type(var_string))
    
    var_string = "Igor Mota"
    print(var_string)
    print(type(var_string))
    
    var_string = '12345'
    print(var_string)
    print(type(var_string))
    
    Ex. string invertido [::-1]
    
    var_string = 'IAN'
    print(var_string[::-1])
    print(type(var_string))
    
    Ex. separar o sobre nome [4:10] onde a primeira letra representa 0
    
    # Igor Mota
    # 0123456789 posiçao
    
    var_string = 'Igor Mota'
    print(var_string[5:9])
    print(type(var_string))
    
(III) - Em Python pode se declar varias variaveis em uma mesma linha.
    
    Ex:
    a1,a2,a3,a4,a5 = 1,2.5,True,2j,'sim'

    print(a2)
    print(type(a2))
    
"""

