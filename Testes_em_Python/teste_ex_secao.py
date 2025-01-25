import unittest

from Exercicio_Secao import Mulher


class ExSecaoTestesMulher(unittest.TestCase):
    
    def setUp(self):
        """ """
        self.ana = Mulher('Ana',60,654123,28)
        self.vanessa = Mulher('Vanessa', 66,654321,8)
        
    def test_aposentadoria_completa(self):
        self.assertEqual(self.ana.aposentadoria(),'Voce pode se aposentar')
        
    def test_aposentadoria_falha(self):
        self.assertEqual(self.vanessa.aposentadoria(),'Ainda não atingiu os requisitos para se aposentar')
        
    def test_salario_aposentadoria_falha(self):
        self.assertEqual(self.vanessa.salario_aposentadoria(),'Você não pode se aposentar')
        
    def test_salario_aposentadoria_concluido(self):
        self.assertEqual(self.ana.salario_aposentadoria(),3600)
        
if __name__ == '__main__': # Essa linha é necessaria pois podemos importar o módulo testes(reaproveitando para outros sistema)
    unittest.main() # Comando para criar a interface e realizar os testes em si
        
        
    