'''
Dict Comprehension

- Representados por chaves {}
- Possuem a relação chave->dado

Como declarar?

Ex A : apenas com (for) - para criar um novo dicionario Dividindo a idade pela metade

pessoas_idade = {'Igor':39,'Ana':41,'Priscila':32}

pessoa_met_idade = {chave: dado // 2 for chave,dado in pessoas_idade.items()}
print(pessoa_met_idade)

mesma coisa que?

pessoas_idade = {'Igor':39,'Ana':41,'Priscila':32}

pessoa_met_idade = {}
for chave,dado in pessoas_idade.items():
    pessoa_met_idade[chave] = dado // 2
print(pessoa_met_idade)

Ex B : com (if e for)  - Para criar um outro dicionario que contenha apenas os maiores de idade

pessoas_idade = {'Igor':22,'Ana':18,'Priscila':14, 'Marcos':19}

maiores_idade = {chave:dado for chave,dado in pessoas_idade.items() if dado >= 18}
print(maiores_idade) 

maiores_idade = {chave:dado for chave,dado in pessoas_idade.items() if dado <= 18}
print(maiores_idade) 

Ex C : com (if, else e for)
# Cria um dicionario com pessoas maiores de idade, mas com um aviso para o menor de idade

pessoas_idade = {'Igor':22,'Ana':18,'Priscila':14, 'Marcos':19}

maiores_idade = {chave:(dado if dado >= 18 else 'Não pode entrar') for chave,dado in pessoas_idade.items()}
print(maiores_idade) 


'''
pessoas_idade = {'Igor':22,'Ana':18,'Priscila':14, 'Marcos':19}

maiores_idade = {chave:(dado if dado >= 18 else 'Não pode entrar') for chave,dado in pessoas_idade.items()}
print(maiores_idade) 

