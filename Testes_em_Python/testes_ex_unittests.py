import unittest

from Exeercicio_Unittest import acordar_cedo, tem_exercicio, tempo_exercicio


class ExercicioUnittestsTestes(unittest.TestCase):
    
    def test_acordar_cedo_tipo(self):
        """ """
        self.assertIs(type(acordar_cedo(10)), str,'Não é string') # Testar se e string
        
    def test_acordar_cedo_falha(self):
        """ """
        self.assertEqual(acordar_cedo(10),'Tente novamente amanhã')
        
    def test_acordar_cedo_concluido(self):
        """ """
        self.assertEqual(acordar_cedo(5), 'Voce é um guerreiro')
        
    def test_tempo_exercicio_concluido(self):
        """ """
        self.assertEqual(tempo_exercicio(67,3),66)
        
    def test_tempo_exercicio_falha(self):
        """ """
        self.assertIsNone(tempo_exercicio(67,1))
        
    def test_tem_exercicio_negativo(self):
        """ """
        self.assertFalse(tem_exercicio('Descanso'))
        
    def test_tem_exercicio_adirmativo(self):
        """ """
        self.assertTrue(tem_exercicio('Natação'))
        
if __name__ == '__main__': # Essa linha é necessaria pois podemos importar o módulo testes(reaproveitando para outros sistema)
    unittest.main() # Comando para criar a interface e realizar os testes em si
        
        
        