'''
Leitura de Arquiuvos Python

- O que sao Arquivos?

Para ler um arquivo de texto puro (.txt) em Python, você pode usar o método open() junto com .read() ou .readlines(). 
Método

Descrição

- read()       Lê o arquivo inteiro de uma vez
- readline()   Lê uma linha completa do arquivo
- readlines()  Lê as linhas remanescentes e retorna como uma lista de linhas

Ex.:

txt
.py

(I) Primeira forma de abrir

# Abrir um arquivo

# Função Open: Recebe como parametro obrigatorio o endereço em que se encontra o arquivo

# Obs.: A abertura padrão é do modo leitura (mode 'r' - read)


caminho_txt = r"C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\arquivo.txt"


with open(caminho_txt, encoding="UTF-8") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
    
(II) Sedunda Forma de Abrir

caminho_txt = r"C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\arquivo.txt"


with open(caminho_txt, encoding="UTF-8") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
        
(III) Teste se o Python consegue encontrar o arquivo
Antes de tentar ler com pandas, teste se o Python consegue localizar o arquivo:

import os

file_path = 'Lista_arquivo.txt'  # Substitua pelo caminho correto
if os.path.exists(file_path):
    print("Arquivo encontrado!")
else:
    print("Arquivo não encontrado!")
    
(IV) Chamar o arquivo todo

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt", 'r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

(V)

from pathlib import Path

root_dir = Path(__file__).parent
mbox_short_file = root_dir / 'Lista_arquivo.txt'

with open(mbox_short_file) as file:
    lines = file.read()

for line in lines:
    line = line.strip()
    print(line, end=' ')

(VI) Forma de leitura

a) Função .read() realiza a leitura do arquivo

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt", 'r', encoding='utf-8')

print(arquivo.read())

arq = arquivo.read()
print(type(arq)) # <class 'str'> pega todo conteudo e armazena em uma string

b) Delimita a quantidade de caracteres (avanço do cursosr)

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt", 'r', encoding='utf-8')

print(arquivo.read(20)) # Determinar o numero de caracter que deseja imprimir

c) Arquivo Fechado ou aberto vai depender de onde esta o print(arquivo.closed)

arquivo = open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt", 'r', encoding='utf-8')

# print(arquivo.closed) # False
arquivo.close() # Finaliza a conexao entre o arquivo aberto e a ide /Fecha o local de arquivo
print(arquivo.closed) # True

(VII) Modo pythonico de trabalhar com arquivos

a) 

# <built-in method read of _io.TextIOWrapper object at 0x0000023966A192A0>
with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt") as lia:
    print(lia.read)
    
b)

# Chama toda a lista
with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt") as lia:
    print(lia.read())

c)

# Chama toda a lista verifica se esta fechada ou aberta
with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt") as lia:
    print(lia.closed) # False
    print(lia.read())
    lia.close()
    print(lia.closed) # True
    
# Chama toda a lista verifica se esta fechada ou aberta
with open("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Lista_arquivo.txt") as lia:
    print(lia.closed) # False
    print(lia.read())
    
    
# -- Quando sai do bloco do (with) ele fecha automaticamente
print(lia.closed) # True
print(lia.read())

False
Janeiro - R$ 8.00,00
Fevereiro - R$ 7.00,00
Marco - R$ 8.500,00
Abril - R$ 9.200,00
Maio - R$ 8.600,00
Junho - R$ 7.950,00
Julho - R$ 8.530,00
Agosto - R$ 9.500,00
Setembro - R$ 10.200,00
Outubro - R$ 9.800,00
Novembro - R$ 8.950,00
Dezembro - R$ 7.560,00
True

'''






