'''
1- Criar um arquivo de texto, iserir o lucro mensal de uma startup entre os meses de janeiro e maio, informando o mes e o valor, 
atraves da entrada do usuario. apos isso ler o arquivo e imprimir o mes de maior lucro.

'''

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\LucroEmpresa.txt', 'w', encoding='utf-8') as LE:
    while True:
        mes = input('Mes: ')
        if mes == 'sair':
            break
        else:
            LE.write(f'{mes}: ')# Escreve o mes no arquivo
            LE.write(input('Lucro: '))
            LE.write('\n')
            
relatorio = {}

with open('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Arquivos\\LucroEmpresa.txt', 'r', encoding='utf-8') as LE:
    for linha in LE:
        relatorio[linha[0:3]] = int(linha[5:]) # A chave do dicionario e o mes (da posição 0 até a 3), e o valor é
# lucro (da posição 5 até o final da linha).

print(relatorio)
maiorLucro = 0
mesMaiorLucro = ''

for mes, lucro in relatorio.items():
    if lucro > maiorLucro:
        maiorLucro = lucro
        mesMaiorLucro = mes
        
        
print(f'Mes com maior lucro: {mesMaiorLucro} com {maiorLucro} reais')


        