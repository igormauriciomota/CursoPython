'''
Exercícios:

1 - Criar uma lista e uma tupla com diversos valores, separar os valores máximos e
mínimos de cada uma em um conjunto. Por fim, verificar se os 4 valores separados
são verdadeiros ou falsos utilizando o any e o all.
Respostas:

# 1

lista = [23, 1, 12, 7.65]
tupla = (0, True, 0.54, 0, 54, True)

#Conjunto que contém os valores máximos e mínimos da lista e da tupla.

conjunto = {max(lista), min(lista), max(tupla), min(tupla)} 

print(conjunto) {0, 1, 54, 23}
print(any(conjunto))  Há pelo menos um valor verdadeiro no conjunto? True
print(all(conjunto))  Todos os valores do conjunto são verdadeiros? False

'''
