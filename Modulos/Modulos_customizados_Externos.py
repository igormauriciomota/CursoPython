'''
Modulos customizados e Externos criados por desenvolvedores Python https://pypi.org/

1º Exemplo: Importando módulos criados por nos (customizado)

import moduloTeste as mo

mo.imparPar(80)
mo.imparPar(81)

print(mo.lista)
for num in mo.lista:
    print(num * 10)

80 é par
81 é impar     
[1, 2, 3, 4, 5]
10
20
30
40
50

2º Exemplo: Modulos Externos -> encontrados na internet, criados por desenvolvedores Python
Obs.: Deixa o código mais visivel, organizado e acessivel.   

# todos os modulos oficiais externos podem ser encontrados em: https://pypi.org/

# Colorama
from colorama import init

init()

'''

from colorama import Back, Fore

print(Fore.RED + 'Some red text')
print(Back.GREEN + 'and with a green backgraound')


