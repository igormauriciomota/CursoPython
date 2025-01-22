'''
Exercícios:
1) Rafael deseja entrar em uma onda fitness, para isso colocou várias metas
como, acordar cedo, definir um tempo de exercício, definir dias de descanso e
qual esporte iria praticar. Para isso aplique o método TDD para criar e testar as
próximas três funções:

a) acordar_cedo: Essa função recebe a hora que ele acordou como parâmetro
e testa se ele acordou após as 6 horas, caso afirmativo retorne ‘Tente
novamente amanhã’, caso contrário ‘Você é um guerreiro’.

b) tempo_exercicio: Essa função recebe a quantidade de horas exercitadas e o
peso (kg) de Rafael, caso o tempo seja inferior a 2 horas, utilize pass, caso
contrário, reduza 1 kg do peso e retorne o valor.

c) tem_exercicio: Função que reconhece se é um dia de descanso ou não,
recebe como parâmetro o esporte que irá praticar no dia, caso receba a string
‘Descanso’ retorna False (Para mostrar que hoje não há exercício), caso
contrário retorna True.

- Nota: Cada aluno poderá desenvolver um conjunto de testes diferente um do outro, 
mas será aplicado uma das possíveis soluções abaixo.

'''

def acordar_cedo(horario):
    if horario > 6:
        return 'Tente novamente amanhã'
    return 'Voce é um guerreiro'


def tempo_exercicio(peso, tempo):
    if tempo > 2:
        peso -= 1
        return peso
    else:
        pass


def tem_exercicio(esporte):
    if esporte == 'Descanso':
        return False
    return True
    
