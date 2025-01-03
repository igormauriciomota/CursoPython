'''
Exercicio Seek, ReadLine e redlines

1 - Crie um arquivo com conteúdo aleatorio. Em seguida, abra o arquivo, leia-o 3 vezes
a partir dos caracteres 5, 9, 14. Por fim feche o arquivo.    

# Mover o cursor para a 5º posição
arqCores = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Cores.txt")
#print(arqCores.read())
arqCores.seek(5)
print(f'\n\n{arqCores.read()}')

# Mover o cursor para a 9º posição
arqCores = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Cores.txt")
#print(arqCores.read())
arqCores.seek(9)
print(f'\n\n{arqCores.read()}')

# Mover o cursor para a 14º posição
arqCores = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Cores.txt")
#print(arqCores.read())
arqCores.seek(14)
print(f'\n\n{arqCores.read()}')

arqCores.close()
--------------------------------------------------------------------

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Cores.txt")

listaLinhas = arquivo.readlines()
print(listaLinhas[3])

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Cores.txt")

listaLinhas = arquivo.readlines()
print(listaLinhas[5])

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Cores.txt")

listaLinhas = arquivo.readlines()
print(listaLinhas[9])

Azul

Preto

Cinza

'''

