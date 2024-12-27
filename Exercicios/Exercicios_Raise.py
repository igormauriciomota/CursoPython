'''
1) A partir do seguinte código aplique raise para apresentar possíveis erros do
seguinte programa que realiza a escolha de uma das opções de lazer para uma
pessoa e dependendo da escolha, chama uma função e realiza testes
específicos.


    
'''

def viagem_exterior(nome,idade,valor):
    print(f'{nome},{idade} anos, tem {valor} para gastar em viagens')
    
def fazer_compras(nome,idade,valor):
    if valor < 200:
        print('Seu orcamento esta curto, cuidado!')
    print(f'{nome},{idade} anos, tem {valor} para gastar em compras')

def cassino(nome,idade,valor):
    if idade < 18:
        print('Você não pode entrar')
    print(f'{nome},{idade} anos, tem {valor} para gastar em cassinos')
    
atividade = input('Digite a opcao que deseja: viajar_exterior, fazer_compras ou cassino \n Opcao:')
if atividade == 'viajar_exterior':
    viagem_exterior(nome='Bruno',idade=26,valor=300.0)
elif atividade == 'fazer_compras':
    fazer_compras(nome='Isabela',idade=40,valor=150.0)
elif atividade == 'cassino':
    cassino(nome='Eduardo',idade=15,valor=100.0)



