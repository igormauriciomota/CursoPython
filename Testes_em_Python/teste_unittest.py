'''
>> E conveniente desenvolver os testes em outro módulo separadamente, criar um modo teste como este 
e comum e organizado;

>> E Recomendado realizar um teste para cada função

verificar as docstrings>python teste_unittest.py -v
'''
import unittest

# Importando os modulos
from Conhecendo_Unittest import converter_padrao, par_impar


# e necessario criar uma class de testes
class ConhecendoUnittestTeste(unittest.TestCase):
    
    #Recebe self porque a classe ConhecendoUnittestTeste herda de Testcase, que por sua vez tem o 
    def test_converte_tarde(self):
        """Testes para horarios vespertinos e noturnos"""
        self.assertAlmostEqual(converter_padrao(14,25), '2:25 P.M', 'Deu Erro')
        
    def test_converte_manha(self):
        """Teste para horarios matutinos"""
        self.assertAlmostEqual(converter_padrao(8,10), '8:10 A.M')
        
    def test_converte_retorno(self):
        """Teste o tipo do retorno da função"""
        self.assertIs(type(converter_padrao(8,10)), str)
        
    def test_par(self):
        """Testa se e par"""
        self.assertTrue(par_impar(4))
        
    def test_impar(self):
        """Testa se e impar"""
        self.assertFalse(par_impar(5))
        


if __name__ == '__main__': # Essa linha é necessaria pois podemos importar o módulo testes(reaproveitando para outros sistema)
    unittest.main() # Comando para criar a interface e realizar os testes em si



