'''
Exercícios:

1 - Kiko precisa invadir uma prisão de segurança extremamente alta para
resgatar Jaiminho. Porém, existem 3 portões protegidos por senhas do TIPO
TUPLA. Cada portão oferece uma dica para descobrir a senha. A dica é
composta por uma tupla contendo algumas dezenas, e uma frase indicando
o processo a ser realizado. Kiko deve criar um programa que imprima na tela
as três senhas no seguinte formato: print(f'Portão X: {senha_do_portão_X}').

# Dicas
Portão 1 = (29, 54, 45) [Alterar todas as dezenas para 0]
Portão 2 = (12, 28, 37, 54) [A soma dos elementos 2 e 3 é o primeiro elemento
da senha, a soma dos elementos 1 e 4 é o segundo elemento da senha]
Portão 3 = (16, 86, 78, 32, 85, 12) [O valor mínimo é o primeiro elemento da
senha, o valor máximo é o segundo elemento da senha]

Result.:

Portão 1: (0, 54, 45)
Portão 1: (0, 0, 45)
Portão 1: (0, 0, 0) 
Portão 2: (65, 66)  
Portão 3: (12, 86)  

'''
portao1 = (29, 54, 45)
portao2 = (12, 28, 37, 54)
portao3 = (16, 86, 78, 32, 85, 12)

# Portao 1
senha1 = list(portao1)
for id in range(0, 3):
    senha1[id] = 0
    
    portao1 = tuple(senha1)
    print(f'Portão 1: {portao1}')
    
# tupla 'portao1' e convertida para a lista 'senha1', assim é possivel 
# editar seus daddos, substituindo todos por 0, em seguida, senha1 e convertida para a tupla portao1 e 
# e impressa abrindo o portao 1

# Portao 2
# São somados os elementos 2 e 3 (28 + 37) da tupla portao2, em seguda os elementos 1 e 4 (12 + 54)tambem são somados, 
# a tupla portao2 e recriada, com os novos valores, e e impressa, abrindo o portao 2.
portao2 = (portao2[1] + portao2[2], portao2[0] + portao2[3])
print(f'Portão 2: {portao2}')

# Portao 3
# A tupla portao3 e recriada com os elementos min e max da tupla;
portao3 = (min(portao3), max(portao3))
print(f'Portão 3: {portao3}')