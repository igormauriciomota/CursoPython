'''
Exercicios de Modulos customizados e Externos

1 - Criar um módulo customizado com duas funçoes (Calculo de quantidade de numeros pares e impares em uma lista qualquer).  
Em seguida execute as funçoes passando como argumento uma lista de números naturais.   



'''

# importando as funçoes do outro módulo

from Modulo_customizado import contaImpares as ci
from Modulo_customizado import contaPares as cp

numeros = [3,5,4,7,32,21,765,86,32,575,12,43,876,87,43,21,3,12,453]

print(cp(numeros))
print(ci(numeros))

