'''
Conhecendo Unittest

O que sõo?

- Módulo para testar individualmente classes, funçoes, metodos, dentre outros

Como trabalhar com eles?

- inicialmente importa-se o modulo unittest e criamos classes que herdam TestCase(Teste de caso) a partir desse módulo
com isso é possivel utilizar todos assertions contidos nele;

> Tabela com todos assertions presentes no módulo: https://docs.python.org/pt-br/3/library/unittest.html#assert-methods

Apresentada a Baixo:

--- Método ---            --- Avalia se ---           

1-assertEqual(a, b)              a == b

2-assertNotEqual(a, b            a != b

3-assertTrue(x)                  bool(x) is True

4-assertFalse(x)                 bool(x) is False

5-assertIs(a, b)                 a is b

6-assertIsNot(a, b)              a is not b

7-assertIsNone(x)                x is None

8-assertIsNotNone(x)             x is not None

9-assertIn(a, b)                 a in b

10-assertNotIn(a, b)             a not in b

11-assertIsInstance(a, b)        isinstance(a, b)

12-assertNotIsInstance(a, b)     not isinstance(a, b)

>> E conveniente desenvolver os testes em outro módulo separadamente

------ Aplicar TDD -------

E convenção nomear cada função dentro do módulo teste iniciando com test_

'''
# Função que converte o padrão 24h para 12h. Ex 16:34 p/ 4:34 PM
def converter_padrao(hora, minuto):
    if hora >= 12:
        hora -= 12
        return f'{hora}:{minuto} P.M'
    return f'{hora}:{minuto} A.M'

# Função que define se e par ou impar, caso for par retorna True, se não retorna False
def par_impar(numero):
    if numero % 2 == 0:
        return True
    return False
    
# E conveniente desenvolver os testes em módulo separado
