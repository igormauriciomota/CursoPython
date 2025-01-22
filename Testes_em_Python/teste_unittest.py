'''
>> E conveniente desenvolver os testes em outro módulo separadamente, criar um modo teste como este 
e comum e organizado;
'''
import unittest

# Importando os modulos
from Conhecendo_Unittest import converter_padrao, par_impar


# e necessario criar uma class de testes
class ConhecendoUnittestTeste(unittest.TestCase):
    
    #Recebe self porque a classe ConhecendoUnittestTeste herda de Testcase, que por sua vez tem o 
    def test_converte_padrao(self):
        self.assertAlmostEqual(converter_padrao(14,25), '2:25 P.M', 'Deu Erro')
        self.assertAlmostEqual(converter_padrao(8,10), '8:10 A.M')
        self.assertIs(type(converter_padrao(8,10)), str)
        
    def test_par_impar(self):
        self.assertTrue(par_impar(4))
        self.assertFalse(par_impar(5))
        

# Comando para criar a interface e realizar os testes em si
if __name__ == '__main__':
    unittest.main()
        
        
    

