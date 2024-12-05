"""
1 - Descubra quais erros estão presentes nos codigos abaixo:

a) Não e possivel transformar letras em inteiros

nome = 'Mark'
print(int(nome))

b) frase invertida forma correta [::-1]

frase = 'Eu sou seu pai'
print(frase[-1::])

c) esta faltando (f'') no inicio antes da string

filme = 'Avatar'
print('A maior bilheteria de 2009
foi {filme}')

d) Esta faltando as aspas ('') em volta do texto input

numero1 = 10
dado = int(input(Digite o numero
que deseja: ))
print(numero1 * dado)

2 - Criação de personagem de mundo de ficção, apresentando opções de acordo
com os tipos das variáveis:

- Cor de Cabelo (string)
- Cor de pele (string)
- Classe: Guerreiro, Mago, Arqueiro (string)
- Idade (int)
- Altura (float)
- Habilidade Específica (string)

Imprima para o usuário o personagem completo.

print('-----Bem Vindo a um novo universo-----')
print('----------Crie seu personagem---------')
nome_personagem = input('Digite o Nome do Personagem: ')
cor_cabelo = input('Digite a cor do cabelo: ')
cor_pele = input('Digite a cor da pele: ')
classe = input('Digite a Classe dentre: 1- Guerreiro\n2 - Mago\n3 - Arqueiro\nopcao: ')
idade = int(input('Digite a Idade: '))
altura = float(input('Digite a Altura: '))
habilidade_especifica = input('Digite sua Habilidade: ')
print('----------Personagem Criado-------------')

print(f'Seu Nome e: {nome_personagem}\n'
      f'Seu personagem tem: \n'
      f'Cabelo de cor: {cor_cabelo}\n'
      f'Pele de cor {cor_pele}\n'
      f'Classe: {classe}\n'
      f'Idade de {idade}\n'
      f'Altura de {altura}\n'
      f'Habilidade de {habilidade_especifica}')


"""

print('-----Bem Vindo a um novo universo-----')
print('----------Crie seu personagem---------')
nome_personagem = input('Digite o Nome do Personagem: ')
cor_cabelo = input('Digite a cor do cabelo: ')
cor_pele = input('Digite a cor da pele: ')
classe = input('Digite a Classe dentre: 1- Guerreiro\n2 - Mago\n3 - Arqueiro\nopcao: ')
idade = int(input('Digite a Idade: '))
altura = float(input('Digite a Altura: '))
habilidade_especifica = input('Digite sua Habilidade: ')
print('----------Personagem Criado-------------')





print(f'Seu Nome e: {nome_personagem}\n'
      f'Seu personagem tem: \n'
      f'Cabelo de cor: {cor_cabelo}\n'
      f'Pele de cor {cor_pele}\n'
      f'Classe: {classe}\n'
      f'Idade de {idade}\n'
      f'Altura de {altura}\n'
      f'Habilidade de {habilidade_especifica}')


