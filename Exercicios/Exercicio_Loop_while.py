"""
1-Faça um programa que calcule o maior polindronmo resultado do produto de dois números de 3 digitos,
- Polindromo são números que lendo da esquerda para a direita resulta no mesmo número caso leia da direita para a esquerda
Ex: 52625
Ex: o maior polindromo resultado do produto de dois números e 91*99 = 9009

n1 = 59
res = 0
while n1 != 0:
    n2 = n1
# Esse loop realiza 999*n2, 998*n2, 997*n2,...até n2 = 0   
    while n2 != 0:
# Esse loop realiza operaçoes n1*999, n1*998, n1*997,....até n2 = 0      
        numero = str(n1 * n2)
        invert_num = numero[::-1]
        if invert_num == numero:
            num = int(numero)
            if res < num:
                res = num
                n2 -= 1
            else:
                n2 -= 1
        else:
            n2 -= 1
    n1 -= 1
print(res)

"""
n1 = 999 # Inicializa o primeiro numero
res = 0 # Inicializa o resultado
while n1 != 99: # Enquanto o primeiro numero for diferente de 99 faça:
    n2 = n1 # Inicializa o segundo numero para fazer n1 * n2
# Esse loop realiza 999*n2, 998*n2, 997*n2,...até n2 = 100  
    while n2 != 99: # Enquanto o segundo numero for diferente de 99 faça:
# Esse loop realiza operaçoes n1*999, n1*998, n1*997,....até n2 = 0      
        numero = str(n1 * n2) # Transforma para string o produto entre n1 e n2 para realizar o comando [::-1]
        invert_num = numero[::-1] # 
        if invert_num == numero: #
            num = int(numero) # volta numero para inteiro
            if res < num: # se resultado for menor que num faça:
                res = num # Armazena num em res pois num e maior
                n2 -= 1
            else:
                n2 -= 1
        else:
            n2 -= 1
    n1 -= 1
print(res)
