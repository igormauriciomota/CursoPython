'''
Seek e ReadLine

(I) seek: Movimenta o cursor pelo arquivo

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt")
print(arquivo.read())

print(arquivo.read())

arquivo.seek(0) # Move o cursor para o inicio do arquivo
print(arquivo.read())

-----------------------------------------------

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt")
print(arquivo.read())

print(arquivo.read())

arquivo.seek(20) # Move o cursor para o Fevereiro do arquivo
print(arquivo.read())

-----------------------------------------------
(II) ReadLine: Le o arquivo por linhas

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt")

linha = arquivo.readline()
print(linha) # Janeiro - R$ 8.00,00

-----------------------------------------------

# A cada comando readline() ele vai buscando a linha

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt")

linha = arquivo.readline()
print(linha) # Janeiro - R$ 8.00,00
linha = arquivo.readline()
print(linha) # Fevereiro - R$ 7.00,00
linha = arquivo.readline()
print(linha) # Marco - R$ 8.500,00  
linha = arquivo.readline()
print(linha) # Abril - R$ 9.200,00 

-----------------------------------------------

(III) readlines: Retorna uma lista que cada elemento e uma linha do arquivo

* readlines() com s

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt")

listaLinhas = arquivo.readlines()
print(listaLinhas)

['Janeiro - R$ 8.00,00\n', 'Fevereiro - R$ 7.00,00\n', 'Marco - R$ 8.500,00\n', 'Abril - R$ 9.200,00\n',
'Maio - R$ 8.600,00\n', 'Junho - R$ 7.950,00\n', 'Julho - R$ 8.530,00\n', 'Agosto - R$ 9.500,00\n',
'Setembro - R$ 10.200,00\n', 'Outubro - R$ 9.800,00\n', 'Novembro - R$ 8.950,00\n', 'Dezembro - R$ 7.560,00']

-----------------------------------------------

linha começa de 0,1,2,3,4....

# Junho - R$ 7.950,00 - busca a quinta linha

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt")

listaLinhas = arquivo.readlines()
print(listaLinhas[5]) 

# Marco - R$ 8.500,00

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt")

listaLinhas = arquivo.readlines()
print(listaLinhas[2]) 


'''


