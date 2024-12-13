
"""
LOOP FOR

Loop e algo que se repete diversas vezes.
Em programação utilizamos eles para repetir uma tarefa várias vezes

O for significa (Para) é uma das ferramentas que realizam esse loop,
- Como declarar for em Python?

for item in sequencia:
    #Processo

significado
Para cada item dentro de uma sequencia faça:
    #Processo
    
A sequencia deve ser "iteravel", mas o que e isso?
- São um conjunto de dados que podem ser desmembrados
Em:

a) String (Pode ser desmembradas por cada caracter)
"Filmes" -> 'F','i','l'...
Relembrando: Podemos pegar caracteres pelos indices da string
Ex:
nome = 'Samantha'
print(nome[6]) # Vai imprimir o h

curiosidade:
print(nome[-1]) # Vai imprimir o a
em Python pode usar ....-3,-2,-1
print(nome[2:-1]) # Vai imprimir manth

b) Listas, tuplas, dicionários e sets(conjuntos):
Ex:
como declarar Listas? Lista comporta varios dados enfilerados
nome = [1,2.5,True,'sim']

c) Função range():
O Que ela faz?

- Função que cria um intervalo de numeros escolhido pelo usuario.
Como declar?
range(numero que voce deseja que comece, numero que voce deseja que finalize + 1)
Ex:
numero = range(2,10) # Cria um intervalo de 2 a 9

#Aplicação com string
seriado = 'Todo mundo odeia o Chris'
for letra in seriado:
    print(letra)
    
#Aplicação com string na mesma linha
seriado = 'Todo mundo odeia o Chris'
for letra in seriado:
    print(letra, end='')
    
#Aplicação com Lista
numeros = [1,2.5,'oi',True]
for elemento in numeros: # Para cada elemento dentro de numeros faça:
    print(elemento)
    
#Aplicação com Range() 
intervalo_num = range(3,11) # Cria uma sequencia de 3 a 10
for numero in intervalo_num: 
    print(numero, end=',')
    
#Aplicação com Range()
intervalo_num = range(10) # Cria uma sequencia de 0 a 9
for numero in intervalo_num:
    print(numero, end=',')
    
#Aplicação com Range(-4,5)
intervalo_num = range(-4,5) # Cria uma sequencia de -4 a 4
for numero in intervalo_num:
    print(numero, end=',')
    
#Aplicação com Range(3,19,3)
intervalo_num = range(3,19,3) # Cria uma sequencia de 3 a 18 ap passo de 3 em 3
for numero in intervalo_num:
    print(numero, end=',')

#Aplicação com Range(3,19,-3)
intervalo_num = range(3,19,-3) # Cria uma sequencia de 3 a 18 ap passo de 3 em 3 negativo
for numero in intervalo_num:
    print(numero, end=',')

(I) È possivel criar uma condicionais dentro de loop

# Achando numeros pares dentro de uma sequencia

num = range(2,20)
for numero in num:
    if numero % 2 == 0: # Se o resto da divisão de numero por 2 for zero faça: 
        print(f'Achei um numero par, numero:{numero}')
        
# Achando numeros pares dentro de uma sequencia
# Nao e necessario criar a varianel (num)

for numero in range(2,20):
    if numero % 2 == 0: # Se o resto da divisão de numero por 2 for zero faça: 
        print(f'Achei um numero par, numero:{numero}')

# Mais complexo buscando a letra (a) da palavra
        
fruta = "abacate"
valor = range(1,4)
for letra in fruta:
    if letra == 'a':
        for num in valor: 
            print('Achei a letra a')

string = 'abcdefghijklmn'

for letra in string:
    print(letra, end='/')
    if letra == 'i':
        break
        ou continue

(II) Metodo enumerate()
    o que e a Função enumerate()?
- Ele adiciona um contador para cada elemento que foi desmembrado na sequencia

# Ex:

heroi = 'Batman'
for valor in enumerate(heroi):
    print(valor)
    
imprime:
(0, 'B')
(1, 'a')
(2, 't')
(3, 'm')
(4, 'a')
(5, 'n')

Para declarar faça:
enumerate(variavel)

# Ex: ao usar o enumerate ele vai criar uma relação entre indice e letra 

heroi = 'Batman'
for valor in enumerate(heroi):
    print(valor)
for contador, letra in enumerate(heroi):
    print(f'A {contador+1} letra e:{letra}')
for valor in enumerate(range(3,7)):
    print(valor)
    
"""


        

