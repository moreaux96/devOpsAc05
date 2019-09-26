from pytest
from com.moreaux.operacoes import Testravis


class TestOperacoes(TestCase):
        
    def setUp(self):
        self.operacoes = Testravis()

    def test_velocidade(self):
        self.assertEqual(self.operacoes.velocidade(100,20),"velocidade: 5.0 m/s")
