'''
Modos de Abertura de Arquivo

Exixtem outros métodos para abertura de arquivos além do 'read' e 'write', eles podem ser consultados 
Em: https://docs.python.org/3/library/functions.html#open


mode é uma string opcional que especifica o modo em que o arquivo é aberto. O padrão é 'r'que significa aberto 
para leitura no modo texto. Outros valores comuns são 'w'para escrita (truncando o arquivo se ele já existir), 
'x'para criação exclusiva e 'a'para anexação (que em alguns sistemas Unix, significa que todas as gravações são 
anexadas ao final do arquivo, independentemente da posição de busca atual). No modo texto, se encoding não for 
especificado, a codificação usada depende da plataforma: locale.getencoding()é chamado para obter a codificação 
de localidade atual. (Para leitura e gravação de bytes brutos, use o modo binário e deixe a codificação não 
especificada.) Os modos disponíveis são:

Personagem

Significado

'r' - aberto para leitura (padrão)

'w' - aberto para escrita, truncando o arquivo primeiro

'x' - aberto para criação exclusiva, falhando se o arquivo já existir

'a' - aberto para escrita, anexando ao final do arquivo se existir

'b' - modo binário

't' - modo de texto (padrão)

'+' - aberto para atualização (leitura e escrita)


O modo padrão é 'r'(aberto para leitura de texto, um sinônimo de 'rt'). Modos 'w+'e 'w+b'abrem e truncam o arquivo. 
Modos 'r+' e 'r+b'abrem o arquivo sem truncamento.

Conforme mencionado na Visão geral , o Python distingue entre E/S binária e de texto. Arquivos abertos no modo 
binário (incluindo 'b'no argumento modebytes ) retornam conteúdos como objetos sem nenhuma decodificação. No modo 
texto (o padrão, ou quando 't'é incluído no argumento mode ), o conteúdo do arquivo é retornado como , os bytes
tendo sido primeiro decodificados usando uma codificação dependente da plataforma ou usando a codificaçãostr 
especificada, se fornecida.

Observação O Python não depende da noção de arquivos de texto do sistema operacional subjacente; todo o 
processamento é feito pelo próprio Python e, portanto, é independente de plataforma.

(I) 'x' - aberto para criação exclusiva, falhando se o arquivo já existir, seja existir erro FileExistsError;

open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\xxxxxx', 'x', encoding='utf-8')

try:
    with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\frutas.txt', 'x', encoding='utf-8') as arq:
        arq.write('Banana\n')
        arq.write('Uva\n')
except FileExistsError:
    print('O arquivo já exixte!')
    
(II) 'a' - aberto para escrita, anexando ao final do arquivo se existir, caso nao exixta ele 
cria um novo e adiciona normalmente, cria um novo e apos play adiciona novamente os mesmsos

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'a', encoding='utf-8') as arq:
    arq.write('Homem Aranha\n')
    arq.write('Hulk\n')
    arq.write('Capitão America\n')
    arq.write('Thor\n')
    arq.write('Homem Formiga\n')
    arq.seek(0) # Não adianta controlar o cursos com o modo 'a', pois sempre imprime no final
    arq.write('Viuva Negra\n')
    
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'a', encoding='utf-8') as arq:
    arq.write(input('Escreva um Heroi: '))    
    
Homem Formiga
Viuva Negra
Homem Aranha
Hulk
Capitão America
Thor
Homem Formiga
Viuva Negra
Capitã MarvelSuper Homem

(III) '+' - aberto para atualização (leitura e escrita)

a) r+ : 

- Error se o arquivo não existir o arquivo deve exixtir - Ele nao adiciona no arquivo ele atualiza

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'r+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    
# 'a' para criar o arquivo
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'r+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    arq.seek(0)                     # temos o controle do cursor e podemos escrever além de ler o arquivo
    arq.write('Batman\n')
    arq.write('Batman\n')
    
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'r+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    arq.seek(0)
    print(arq.read())


b) w+ : 

- Cria um novo arwuivo caso nao exixta e sobrescreve o texto caso já exista

- Tambem realiza leitura alem da escrita de arquivos

- temos o controle do cursor e podemos escrever além de ler o arquivo

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'w+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'w+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    arq.seek(6)
    print(arq.read())

d) a+ :

- Cria um novo arquivo caso nao exista

- Adiciona o texto no final caso já exista

- realiza a leitura e escrita

- o cntrole do cursor apena para a leitura, Não temos o controle do cursor na escrita

# 'a+' Cria um arquivo caso nao exixta
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'a+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    
c) x+ :

- Cria um novo arquivo caso não exixta

- Error se o arquivo já existir: FileExistsError

- So funcionara a impressao caso o arquivo não exista

- so podemos realizar leitura e escrita

- Temos o controle do cursor tanto pra escrita quanto para leitura/ arquivo nao pode existir

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'x+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'x+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    arq.seek(0)
    print(arq.read())    
    
with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\herois.txt', 'x+', encoding='utf-8') as arq:
    arq.write('Gavião Arqueiro\n')
    arq.write('Soldado Invernal\n')
    arq.seek(0)
    arq.write('Soldado Invernal\n')  
    
'''

