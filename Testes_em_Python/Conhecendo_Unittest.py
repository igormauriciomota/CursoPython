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

1-Função que converte o padrão 24h para 12h. Ex: 16:34 p/ 4:34 P.M



2-Função que define se é par ou impar, caso for par retorna True, se não retorna False


'''
#1
def converter_padrao(hora, minuto):
    pass


def par_impar(numero):
    pass
    

