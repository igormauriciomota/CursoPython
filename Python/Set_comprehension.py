'''
Sets Comprehension

- Não possuem ordnação
- Não possuem elementos repetidos
- são declarados por chaves {}

Ex: 1

Obs.: o elemento que vai receber no inicio depois vem o (for) repete elemento (in) variavel

trava_linguas = 'O Rato roeu a roupa do rei de roma'
conjunto = {letra for letra in trava_linguas}
print(conjunto)

{'i', 'r', 'o', 'm', 'R', 'e', 'u', 'd', 'O', 'a', ' ', 't', 'p'}
Desordenado e sem letras repetidas letra maiuscula e minuscula são tratados de forma diferente

para ue seja considerado um conjunto deve ser da segunte forma

conjunto = set() # forma correta
conjunto = {} # forma errada

Ex: 2 range()

# conjunto numero impares de 1 a 20;
conjunto_impares = {numero for numero in range(1,21,2)}
print(conjunto_impares)

{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

# conjunto numero impares de 1 a 20, numero de preferencia entre for e if
conjunto_impares = {numero for numero in range(1,21) if numero % 2 != 0}
print(conjunto_impares)

-> Desafio faça usando comprehension de conjuntos imprimir os multiplos de 3, porem os não multiplos 
devem ser impressos com a mensagem print(f'Desconhecido:{numero}')


multiplos_3 = {numero if numero % 3 == 0 else print(f'Desconhecido:{numero}') for numero in range(1,22)}
print(multiplos_3)

{None, 3, 6, 9, 12, 15, 18, 21}


multiplos_3 = {print(numero) for numero in range(1, 22) if numero % 3 == 0}
print(multiplos_3)

{None, 3, 6, 9, 12, 15, 18, 21}
'''

multiplos_3 = {print(numero) for numero in range(1, 22) if numero % 3 == 0}
print(multiplos_3)
