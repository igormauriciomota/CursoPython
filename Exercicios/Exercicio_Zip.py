'''
Exercícios Zip:

1 - Está acontecendo uma gincana na Escola e você foi escolhido(a) para
realizar o controle da pontuação! Para isso, crie 4 listas (A primeira com nome
das pessoas que participam da gincana. As outras 3 (cada uma representando
uma prova) armazenam valores de 0 a 100, ou seja, as notas que cada
participante obteve. Por fim, utilize zip() para retornar um dicionário
com o nome de cada aluno como chave e o somatório de suas notas em cada
prova como valor. Após isso, imprima o participante vencedor.

'''

nomes = ['Maria', 'Pedro', 'Napoleão', 'Chaves', 'Jhennifer']
nota1 = [3.8, 6, 9, 8, 7.5]
nota2 = [7.6, 6.3, 8, 7, 8.2]
nota3 = [5.5, 3.5, 2.8, 6, 4.2]

listaNotas = []

tabela = zip(nota1, nota2, nota3) # Agrupa as notas das 3 provas em uma tupla para cada participante

for notas in tabela:
    listaNotas.append(sum(notas)) # Soma as notas das 3 provas de cada participante e coloca na lista
    # numeros nao podem ser somados com string ''
    
tabelaFinal = zip(nomes, listaNotas) # ASSOCIA O NOME DE CADA PARTICIPANTE COM SUA RESPECTIVA NOTA FINAL

dicioFinal = dict(tabelaFinal)

vencedor = ''
pontos = 0

for part, pts in dicioFinal.items():
    print(f'Participante: {part}. Pontos: {pts}')
    if pts > pontos:
        pontos = pts
        vencedor = part
        
print(f'\n___ vencedor: {vencedor} - Pontos: {pontos}____')

