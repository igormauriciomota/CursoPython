'''
Escrita em Arquivos

Obs.: Ao abrir um arquivo pelo modo padrão, é possivel apenas realizar a leitura.  
# arquivo = open('')

- Para escrita, é necessario alterar o modo de abertura de 'r' para 'w' - write

Obs.: Sempre que houver escrita em um arquivo pelo modo 'w', ele será criado 
cado nao existir, caso ja exista, seu conteudo sera substituido completamente

(I) Escrever em arquivos

Apresenta o erro: Usando open sem especificar explicitamente uma codificação Pylint W1514:unspecified-encoding
para evitar utilizar o -> encoding='utf-8'

a) Desta forma foi criado o arquivo -> Despesas.txt

arquivo = open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Despesas.txt', 'w', encoding='utf-8')

arquivo.write('Café: R$ 15.800,00')
arquivo.write('\nBiscoitos: R$ 24.350,00')

arquivo.close()

arquivo = open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Despesas.txt', 'w', encoding='utf-8')

arquivo.write('\nBolachas: R$ 12.000,00')
arquivo.close()

(II) # Modo pythonico de trabalhar com arquivos

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Despesas.txt', 'w', encoding='utf-8') as desp:
    desp.write('Café: R$ 15.800,00')
    desp.write('\nBananas: R$ 4.500,00')

'''


with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\Despesas.txt', 'w', encoding='utf-8') as desp:
    while True:
        palavra = input("Digite uma palavra ou 'sair': ")
        if palavra == 'sair':
            break
        else:
            desp.write(palavra + '\n')
            



