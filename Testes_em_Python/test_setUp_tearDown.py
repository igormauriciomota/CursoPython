import unittest

from SetUp_TearDown import BolsaDeValores


class SetUpTearDownTestes(unittest.TestCase):

    def setUp(self):
        print('Iniciando Teste')
        self.pessoa = BolsaDeValores('Mario', 123456)

    def test_deposito_falha(self):
        self.assertEqual(self.pessoa.deposito(-100),'O valor de depósito deve ser positivo')

    def test_deposito_concluido(self):
        self.pessoa.deposito(100)
        self.assertEqual(self.pessoa.saldo,100)

    def test_compra_acao_concluido(self):
        self.pessoa.deposito(100)
        self.pessoa.compra_acao('Weg')
        self.assertEqual(self.pessoa.saldo,65)

    def test_compra_acao_falha(self):
        self.assertEqual(self.pessoa.compra_acao('Weg'),'Dinheiro insuficiente para compra, vá para o mercado fracionário')

    def tearDown(self):
        print('Teste Finalizado')

if __name__ == '__main__':
    unittest.main()
