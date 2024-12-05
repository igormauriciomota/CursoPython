
"""
 I - Relacione as colunas de acordo com o tipo da variavel.

(1) Inteiro                        (5) "Casa"
                                   (3) 2 + 0j
(2) Float                          (4) True
                                   (5) '123'
(3) Complexo                       (2) 1.2345
                                   (4) False
(4) Booleano                       (5) '"2j"'
                                   (3) 10 + 1j
(5) String                         (1) 2
       
                                   (5) 'Programando Ideias'
Ex. conferir as respostas

teste = "casa"
print(type(teste))

II - Faça um programa que receba o nome de um aluno e quanto ele tirou na prova de programação, depois
imprima em apenas uma linha o nome no mod title() e quanto a pessoa tirou na prova. Ex: Ana Carolina tirou 8;

# Com a função input() voce consegue pegar dados do usuario
nome = input('Digite o nome do aluno/a: ')
nota = input('Digite a nota do aluno/a: ')
print(f'{nome.title()} tirou a nota {nota}')

"""

# Com a função input() voce consegue pegar dados do usuario
nome = input('Digite o nome do aluno/a: ')
nota = input('Digite a nota do aluno/a: ')
print(f'{nome.title()} tirou a nota {nota}')
