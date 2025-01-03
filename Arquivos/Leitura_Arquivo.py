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
        
(III) Terceira forma

'''




