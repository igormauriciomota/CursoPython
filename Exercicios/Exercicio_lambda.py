
'''
1 - Criar duas listas de mesmo tamanho preenchidas com números inteiros e retornar outra lista com
a soma das duas listas sendo uma delas invertida (indice 0 com indice 9 para uma lista de tamanho 10,
por exemplo), utilizando lambda e comprehension para iteraar em ambas;

lista2.reverse()#Inverte os valores da lista
soma = lambda lista1, lista2: [lista1[ind] + lista2[ind] for ind in range(0, 10)]
# soma os elementos correspondentes das listas. ex; Elemento 0 (10) + Elemento 0 (217)...   
print(soma(lista1, lista2))
lista3.append(soma(lista1, lista2))
print(sum(soma(lista1, lista2)))
print(min(soma(lista1, lista2)))
print(max(soma(lista1, lista2)))

[227, 562, 54, 28, 74, 103, 92, 130, 101, 260]
1631
28  
562 

'''



