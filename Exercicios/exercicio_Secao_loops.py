"""
1 - Media dos 5 primeiros números primos da sequencia Fibonacci

- O que e a sequencia de Fibonacci?
1,1,2,3,5,8,13,21,34,55,.....

anterior = 0
proximo = 1
parada = 1
while parada <= 10:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    parada = parada + 1

Agora aplicando a condição de ser numero primo:
- condição:
a) Numero primos devem ser maiores do que 1
b) Numeros primos são apenas divisiveis por ele mesmo e o numero 1

Ex: 5,8,13,21,34,55,89

anterior = 0
proximo = 1
parada = 1
while parada <= 5:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    divisor = 1
    nun_div_int = 0
    while divisor <= proximo:
        if proximo % divisor == 0:
            nun_div_int += 1
        divisor += 1
    if nun_div_int == 2:
        print(proximo)
        parada += 1
        
"""
anterior = 0
proximo = 1
parada = 1
while parada <= 5:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    divisor = 1
    nun_div_int = 0
    while divisor <= proximo:
        if proximo % divisor == 0:
            nun_div_int += 1
        divisor += 1
    if nun_div_int == 2:
        print(proximo)
        parada += 1
        
    