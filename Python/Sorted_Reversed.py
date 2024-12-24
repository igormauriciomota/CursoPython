'''
Sorted e Reversed

(I) sorted: semelhante ao sort é utilizado apenas em listas e o sorted em qualquer iteravel

# Exemplo de sorted

notas_list = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
print(sorted(notas_list))

notas_tuplas = (10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3)
print(sorted(notas_tuplas))

notas_conjuntos = {10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3}
print(sorted(notas_conjuntos))

# Sorted retorna uma lista com elementos de um iteravel ordenados

[0, 1, 3, 3, 6, 7, 8, 8.8, 9, 10]
[0, 1, 3, 3, 6, 7, 8, 8.8, 9, 10]
[0, 1, 3, 6, 7, 8, 8.8, 9, 10] -> conjunto nao há repetição

# Inverter o sorted
print(sorted(notas_tuplas, reverse=True))

[10, 9, 8.8, 8, 7, 6, 3, 3, 1, 0]

(II) Reversed: semelhante ao reverse. Porem reverse é utilizado apenas em listas e reversed em qualquer iteravel

- Retorna um objeto do tipo list_reverseiterator com os elementos de um iteravel revertidos/invertidos
# Exemplo de reversed

# Lista
notas_list = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
print(reversed(notas_list))
print(list(reversed(notas_list)))

# Tuplas
notas_tuplas = (10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3)
print(reversed(notas_tuplas))
print(list(reversed(notas_tuplas)))

# Conjuntos não tem indice (NÂO FUNCIONA)

notasC = {10, 7, 8.8, 3, 8, 6, 9, 1, 0}
print(reversed(notasC)) -> TypeError: conjunto = 'set' object is not reversible

<list_reverseiterator object at 0x000001EB78B85CC0>
[3, 0, 1, 9, 6, 8, 3, 8.8, 7, 10]      
<reversed object at 0x000001EB78B85D20>
[3, 0, 1, 9, 6, 8, 3, 8.8, 7, 10] 

# Iterar sobre o reversed
notasLista = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
for nota in reversed(notasLista):
    print(nota, end=' ')
    
# 3 0 1 9 6 8 3 8.8 7 10
'''

    



