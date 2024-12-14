"""
Exercícios:
1) Faça um programa que contabiliza time de heróis e vilões da seguinte forma:
- Crie um dicionário chamado herói com chave sendo o nome do personagem e
o elemento o nível de poder do personagem entre 1 a 100. Ex: herói =
{‘Flash’:85}.

- Crie outro dicionário que serão as armas que podem ser usadas pelo herói,
sendo a chave o nome da arma e o elemento o nível de poder de 0 a 100. Ex:
arma = {‘Escudo do Capitão América’:60}

- Crie um último dicionário representado os vilões sendo a chave o nome e o
elemento o nível de poder de 0 a 200. Ex: vilao={‘Thanos’:175}

Após isso o usuário poderá escolher um herói, uma arma soma os pontos de
poder e escolher um vilao para lutar, apresente quem foi o vencedor, caso for o
herói imprima a arma usada. Caso resulte em empate informe na saída.

Observação: Pode definir qualquer herói,vilao e arma que quiser.

"""
herois = {'Homem de Ferro':80, 'Capitam Marvel':98, 'Thor':90, 'Goku':100}
armas = {'Mionir':90, 'Hukebaster': 95, 'Escudo':85, 'Raio de zeus': 98, 'Kaioken':98}
viloes = {'Dike vigarista':85, 'Venon':145, 'Thanos':180, 'Friza':165, 'Ultron':182}

herois_escolhido = input('Digite o heroi escolhido: ')
arma_sescolhida = input('Digite a arma escolhida: ')
vilao_escolhido = input('Digite o vilao escolhido: ')

nivel_poder_heroi = herois[herois_escolhido] + armas[arma_sescolhida]

if nivel_poder_heroi > viloes[vilao_escolhido]:
    print(f'O vencedor é {herois_escolhido} com {arma_sescolhida}')
elif nivel_poder_heroi == viloes[vilao_escolhido]:
    print('Deu empate!')
else:
    print(f'O Vilão {vilao_escolhido} Venceu a luta, Planeta em perigo!')

# Resposta?

# Digite o heroi escolhido: Goku
# Digite a arma escolhida: Kaioken
# Digite o vilao escolhido: Thanos
# O vencedor é Goku com Kaioken