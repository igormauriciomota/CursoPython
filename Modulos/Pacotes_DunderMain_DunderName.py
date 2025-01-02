
'''
Pacotes, Dunder Main e Dunder Name

- Pacotes são um conjunto de módulos
- Pacotes são pastas

# Obs.: O Módulo __init__.py e criado automaticamente, e por convenção e compatibilidade, não e utilizado.  

(I)

# Importar um modulo de pacotes

from PACOTE1 import Arquivo1

Arquivo1.intro()

(II)

# Importar um modulo de pacote dentro de outro pacote

from PACOTE1.PACOTE2 import Arquivo2

Arquivo2.soma(10, 18)

(III)

# Importar um modulo de pacote dentro de outro pacote

from PACOTE1.Arquivo1 import intro

intro()

(IV)

from PACOTE1.PACOTE2.Arquivo2 import soma

soma(10, 20)

/// Dunder Main e Dunder Name

a) Dunder(__): Double Under (Underline 2 x)
b) Dunder Main: __main__
c) Dunder Name: __name__

# em C:

int main(){
    # Tudo Aqui
}

# em Python: Atribui o valor __main__ para a variavel __name__

Print(__name__)

from PACOTE1 import Arquivo1

Arquivo1.intro()

PACOTE1.Arquivo1
Olá, estamos em outro módulo!


'''




