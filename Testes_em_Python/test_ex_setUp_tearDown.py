import unittest

from Exercicio_SetUp_TearDown import Tatu


class ExSetUpTearDownTestes(unittest.TestCase):
    
    def setUp(self):
        self.bola = Tatu('Bola')
        self.napoleao = Tatu('Napoleao')
        
    def test_comer(self):
        self.assertEqual(self.bola.comer(),'Sou Bola e estou comendo pizza')
        
    def test_beber(self):
        self.assertEqual(self.napoleao.beber(), 'Sou Napoleao e estou bebendo suco')
        
    def test_cavar(self):
        self.assertEqual(self.bola.cavar(),'Sou Bola e estou cavando sua grama')
        
    def test_acasalar(self):
        self.assertEqual(self.napoleao.acasalar(),'Sou Napoleao e quero um filhote')
        
    def tearDown(self):
        print('Teste Concluido')
        
if __name__ == '__main__':
    unittest.main()
    
    
