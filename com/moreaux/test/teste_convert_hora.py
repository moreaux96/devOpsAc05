from pytest
from com.moreaux.convert_hora import ConvertHr


class ConverteHora(ConvertHr):
        
    def setUp(self):
        self.convert_hora = ConvertHr()

    def test_velocidade(self):
        self.assertEqual(self.convert_hora.converteHora(16,01),"%02d:%02d PM 5.0 m/s")
