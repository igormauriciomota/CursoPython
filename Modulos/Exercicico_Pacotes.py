'''
1 - Crie uma pasta, uma subpasta e em seguida um modulo na subtasta contendo uma função qualquer,
Acesse o modulo no programa principal e execute a função;

Obs.: No modulo criad, estabeleça uma condição para a função ser acessada apenas se o modulo for
importado e executado em outro, ou seja, quando o módulo em questão não e o principal (main).   

'''

from random import choice as ch

from PacoteFora.PacoteDentro.ModuloDentro import preverFuturo

idades = [44, 40, 37, 14, 45, 42, 46, 41, 54, 43, 56, 55, 39, 48, 65, 52]
formacao = ['Desingner', 'Analista de sistemas', 'Programador', 'Professor', 'Engenheiro', 'Arquiteto']
trabalho = ['Diretor', 'Programador PHP', 'Desenvolvedor', 'Analista', 'FullStack', 'frontEnd', 'BackEnd','Programador Python' ]
pais = ['França', 'Alemanha', 'Escocia', 'Inglaterra', 'Espanha']
animal = ['Cachorro', 'Gato', 'Coelho', 'Peixe', 'Tartaruga', 'Ramister', 'Passaro']
nome = input('Digite um Nome: ')

preverFuturo(nome, ch(idades), ch(formacao), ch(trabalho), ch(pais), ch(animal))

