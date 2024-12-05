"""
Estruturas Lógicas

a) and (e): True apenas se todas as condiçoes forem True (Verdadeira)

    # Exemplo 1
    # Segurança de sensor: 60 a 75
    sensor = int(input('Digite o Padrao:'))

    if sensor >= 60 and sensor <= 75:
        print('Tudo certo!')
    else:
        print('Risco de acidente!')

    # Exemplo 2
    agua = True
    comida = False

    if agua and comida:
        print('Cachorro feliz!')
    else:
        print('cachorro Triste!')

b) or (ou): True quando pelo menos uma condição for True

    # Ex. 1
    pizza = True
    lasanha = True

    if pizza or lasanha:
        print('Preciso comer mais salada')
    else:
        print('Estou com fome!')

    ----------------------------
    # Ex. 2

    num = 23

    if num % 2 == 0 or num < 10:
        print('E par ou menor que 10')
    else:
        print('E impar e maior ou igual a 10')

c) is (e): Comparação entre valores, similar ao ==

Ex. 1
login = False

print(login is True) # login é True? R: Não (False)
print(login is False) # Login é False? R: Sim (True)

Ex. 2
login = False

if login is True:
    print('Logado')
else:
    print('Deslogado')

d) not (não): Inversão do valor booleano (True -> False, False -> True)

login = False

if not login: # não False: True
    print('Deslogado')
else:
    print('Logado')

"""



