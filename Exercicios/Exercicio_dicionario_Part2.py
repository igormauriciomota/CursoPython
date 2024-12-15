'''
1 - Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente
em cima da hora. Ele resolveu comprar um tipo de flor, um presente e escolher
um lugar para saírem, ele anotou todas as opções abaixo:

Flores

Tipo                  Preço
Rosas Vermelhas       145,00
Girassóis             125,00
Margaridas            120,00
Flores do campo       140,00

Presente

Tipo                  Preço
Urso de Pelúcia       55,00
Caixa de Bombom       60,00
Colar                 75,00
Roupas                40,00

Lugar

Tipo                  Preço
Praia                 70,00
Sair para jantar      150,00
Parque de diversões   120,00
Hotel                 180,00

- Crie um programa que descubra qual a combinação mais cara, em seguida
mais barata e a média opção. Imprima a combinação em cada caso.

- Use um dicionário para cada item (flor, lugar e presente).

-------------//--------------

.items() - nos permite acessar de maneira mais fácil as chaves e os valores existentes em um dicionário. 
Quando pegamos um dicionário e utilizamos o . items() isso irá retornar uma lista contendo pares de tuplas, 
onde, em cada uma dessas tuplas, o primeiro elemento será a chave do dicionário e o segundo elemento o valor.

'''
flores = {'Rosas Vermelhas':145,'Girassois':125,'Margarida':120,'Flores do campo':140}
prersentes = {'Urso pelucia':55,'Bombom':60,'Colar':75,'Roupa':40}
lugares = {'Praia':70,'Jantar':150,'Parke':120,'Hotel':180}

# Encontrar a combinação mais cara:
preco_total = 0
flor_cara = ''
presente_caro = ''
lugar_caro = ''

for flor,valor in flores.items():
    for presente,preco in prersentes.items():
        for lugar,custo in lugares.items():
            preco_atual = valor + preco + custo
            if preco_atual > preco_total:
                preco_total = preco_atual
                flor_cara = flor
                presente_caro = presente
                lugar_caro = lugar
                
print(f'Custo total R$ {preco_total}, Flor: {flor_cara}, Presente: {presente_caro}, Lugar: {lugar_caro}')
# Result: Custo total R$ 400, Flor: Rosas Vermelhas, Presente: Colar, Lugar: Hotel

# Encontrando a combinação mais barata

aux = 0
preco_total = 0
flor_barata = ''
presente_barato = ''
lugar_barato = ''

for flor,valor in flores.items():
    for presente,preco in prersentes.items():
        for lugar,custo in lugares.items():
            if aux == 0:
                preco_total = valor + preco + custo
                aux += 1
            else:
                preco_atual = valor + preco + custo
                if preco_atual < preco_total:
                    preco_total = preco_atual
                    flor_barata = flor
                    presente_barato = presente
                    lugar_barato = lugar
                
print(f'Custo total R$ {preco_total}, Flor: {flor_barata}, Presente: {presente_barato}, Lugar: {lugar_barato}')
# Result: Custo total R$ 230, Flor: Margarida, Presente: Roupa, Lugar: Praia

# Encontrar a media de opção de preço:
preco_total = 0
list = []

for flor,valor in flores.items():
    for presente,preco in prersentes.items():
        for lugar,custo in lugares.items():
            list.append(valor + preco + custo)
list.sort()
preco_total = list[len(list) // 2]

for flor,valor in flores.items():
    for presente,preco in prersentes.items():
        for lugar,custo in lugares.items():
            if valor + preco + custo == preco_total:
                print(f'Custo Medio total R$ {preco_total}, Flor: {flor}, Presente: {presente}, Lugar: {lugar}')
            
# Result:
# Custo Medio total R$ 325, Flor: Rosas Vermelhas, Presente: Bombom, Lugar: Parke 
# Custo Medio total R$ 325, Flor: Margarida, Presente: Urso pelucia, Lugar: Jantar
