'''
1 - A partir da lista apresentada, criar um Generator contendo apenas animais que comecen com 
'C' ou 'A' e que o tamanho de seu nome seja maior que 5, por fim itere e imprima o Generator.  


and - Retorna True se todas as condições forem verdadeiras, caso contrário retorna False
or - Retorna True se uma das condições for verdadeiras, caso contrário retorna False
not - Inverte o resultado: se o resultado da expressão for True, o operador retorna false

'''
# Lista de Animal
listaAnimais = ('Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelha',
                'Carneiro', 'Cabra', 'Coelho', 'Zebra', 'Macaco', 'Peixe', 'Aranha')
# generator          para cada animal na lista 'listaAnimais' se o nome do animal começar com (C) ou (A) 
# nome do animal mais que 5 letras imprima;


genAnimais = (animal for animal in listaAnimais if (animal[0] == 'C' or animal[0] == 'A') and len(animal) > 5)
print(genAnimais)

# Iterar e imprimir o generator
for animal in genAnimais:
    print(animal, end=', ')
