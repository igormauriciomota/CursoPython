'''
Zip

- Retorna um objeto zip com elementos dos iteraveis passados como parametros.  
- Pode receber qualquer tipo de iteravel.  
- O tamanho do menor iteravel predomin.  

Ex.:

alunos = ['Bianca', 'Vitor', 'Ariel']
notas = (10, 6, 8)

juntarTudo = zip(alunos, notas)
# print(list(juntarTudo)) # transforma em uma lista
print(dict(juntarTudo)) # transforma em um dicionario chave/valor {'Bianca': 10, 'Vitor': 6, 'Ariel': 8}
print(type(juntarTudo))

Result:
[('Bianca', 10), ('Vitor', 6), ('Ariel', 8)]
<class 'zip'>

nome = ['Bianca', 'Vitor', 'Ariel', 'José']
idade = (18, 82, 71, 9, 12)
cidade = {'São Paulo', 'Vitoria', 'São Luiz'}
estado = {1:'RS', 2:'PR', 3:'ES', 4:'AM'}

print(list(zip(nome, idade, cidade, estado.values()))) # - O tamanho do menor iteravel predomin.(cidade)


[('Bianca', 18, 'São Luiz', 'RS'), ('Vitor', 82, 'São Paulo', 'PR'), ('Ariel', 71, 'Vitoria', 'ES')]

--------------------------------------------------------------



lugares = [ ('SP', 'São Paulo'), ('ES', 'Vitoria'), ('RS', 'Porto Alegre')]

# *lugares -> ('SP', 'São Paulo'), ('ES', 'Vitoria'), ('RS', 'Porto Alegre') separa as 3 tuplaas
# zip ->  pegar o primeiro elemento de cada tupla ('SP', 'ES', 'RS')

print(list(zip(*lugares)))

resposta: [('SP', 'ES', 'RS'), ('São Paulo', 'Vitoria', 'Porto Alegre')]

'''

lugares = [ ('SP', 'São Paulo'), ('ES', 'Vitoria'), ('RS', 'Porto Alegre')]

print(list(zip(*lugares)))


