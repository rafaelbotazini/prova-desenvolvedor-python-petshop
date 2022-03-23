from datetime import datetime
from unittest import TestCase, main
from unittest.mock import patch
from canil import obter_orcamento_banhos

from petshop import MeuCaninoFeliz, PetShop, ChowChawgas, TamanhoCachorro, VaiRex, eh_dia_de_semana


class TestPetshop(TestCase):
    dias_de_semana = [
        datetime(2022, 3, 21),  # segunda
        datetime(2022, 3, 22),  # terca
        datetime(2022, 3, 23),  # quarta
        datetime(2022, 3, 24),  # quinta
        datetime(2022, 3, 25),  # sexta
    ]

    final_de_semana = [
        datetime(2022, 3, 26),  # sabado
        datetime(2022, 3, 27),  # domingo
    ]

    def test_eh_dia_de_semana(self):
        for dia in self.dias_de_semana:
            self.assertTrue(eh_dia_de_semana(dia))

        for dia in self.final_de_semana:
            self.assertFalse(eh_dia_de_semana(dia))

    def test_petshop(self):
        petshop = PetShop(nome='petshop', distancia_metros=100, preco_banho_grande=10, preco_banho_pequeno=5)

        self.assertEqual(100, petshop.distancia_metros)
        self.assertEqual(5, petshop.get_preco_banho(TamanhoCachorro.PEQUENO))
        self.assertEqual(10, petshop.get_preco_banho(TamanhoCachorro.GRANDE))

    def test_chowchawgas(self):
        petshop = ChowChawgas()

        self.assertEqual(800, petshop.distancia_metros)

        for dia_semana in self.dias_de_semana:
            self.assertEqual(30, petshop.get_preco_banho(TamanhoCachorro.PEQUENO, dia_semana))
            self.assertEqual(45, petshop.get_preco_banho(TamanhoCachorro.GRANDE, dia_semana))

        for dia_fds in self.final_de_semana:
            self.assertEqual(30, petshop.get_preco_banho(TamanhoCachorro.PEQUENO, dia_fds))
            self.assertEqual(45, petshop.get_preco_banho(TamanhoCachorro.GRANDE, dia_fds))

    def test_vairex(self):
        petshop = VaiRex()

        self.assertEqual(1700, petshop.distancia_metros)

        for dia_semana in self.dias_de_semana:
            self.assertEqual(15, petshop.get_preco_banho(TamanhoCachorro.PEQUENO, dia_semana))
            self.assertEqual(50, petshop.get_preco_banho(TamanhoCachorro.GRANDE, dia_semana))

        for dia_fds in self.final_de_semana:
            self.assertEqual(20, petshop.get_preco_banho(TamanhoCachorro.PEQUENO, dia_fds))
            self.assertEqual(55, petshop.get_preco_banho(TamanhoCachorro.GRANDE, dia_fds))

    def test_meucaninofeliz(self):
        petshop = MeuCaninoFeliz()

        self.assertEqual(2000, petshop.distancia_metros)

        for dia_semana in self.dias_de_semana:
            self.assertEqual(20, petshop.get_preco_banho(TamanhoCachorro.PEQUENO, dia_semana))
            self.assertEqual(40, petshop.get_preco_banho(TamanhoCachorro.GRANDE, dia_semana))

        for dia_fds in self.final_de_semana:
            self.assertEqual(24, petshop.get_preco_banho(TamanhoCachorro.PEQUENO, dia_fds))
            self.assertEqual(48, petshop.get_preco_banho(TamanhoCachorro.GRANDE, dia_fds))

class TestCanil(TestCase):
    @patch('canil.obter_petshops')
    def test_obter_orcamento_banhos_grande(self, mock_obter_petshops):
        ps1 = PetShop(nome="petshop 1", distancia_metros=300, preco_banho_grande=40, preco_banho_pequeno=10)
        ps2 = PetShop(nome="petshop 2", distancia_metros=300, preco_banho_grande=50, preco_banho_pequeno=10)

        mock_obter_petshops.return_value = [ps1, ps2]
        data = datetime(2022, 3, 21)

        expected = (ps1, 80)
        actual = obter_orcamento_banhos(data, qt_pequenos=0, qt_grandes=2)

        self.assertEqual(expected, actual)

    @patch('canil.obter_petshops')
    def test_obter_orcamento_banhos_pequeno(self, mock_obter_petshops):
        ps1 = PetShop(nome="petshop 1", distancia_metros=300, preco_banho_grande=40, preco_banho_pequeno=25)
        ps2 = PetShop(nome="petshop 2", distancia_metros=300, preco_banho_grande=40, preco_banho_pequeno=15)

        mock_obter_petshops.return_value = [ps1, ps2]
        data = datetime(2022, 3, 21)

        expected = (ps2, 30)
        actual = obter_orcamento_banhos(data, qt_pequenos=2, qt_grandes=0)

        self.assertEqual(expected, actual)

    @patch('canil.obter_petshops')
    def test_obter_orcamento_banhos_menor_valor(self, mock_obter_petshops):
        ps1 = PetShop(nome="petshop 1", distancia_metros=300, preco_banho_grande=50, preco_banho_pequeno=20)
        ps2 = PetShop(nome="petshop 2", distancia_metros=300, preco_banho_grande=40, preco_banho_pequeno=10)

        mock_obter_petshops.return_value = [ps1, ps2]
        data = datetime(2022, 3, 21)

        expected = (ps2, 110)
        actual = obter_orcamento_banhos(data, qt_pequenos=3, qt_grandes=2)

        self.assertEqual(expected, actual)

    @patch('canil.obter_petshops')
    def test_obter_orcamento_banhos_menor_distancia(self, mock_obter_petshops):
        ps1 = PetShop(nome="petshop 1", distancia_metros=300, preco_banho_grande=30, preco_banho_pequeno=15) # $120
        ps2 = PetShop(nome="petshop 2", distancia_metros=100, preco_banho_grande=50, preco_banho_pequeno=20) # $180
        ps3 = PetShop(nome="petshop 3", distancia_metros=150, preco_banho_grande=40, preco_banho_pequeno=10) # $120

        mock_obter_petshops.return_value = [ps1, ps2, ps3]
        data = datetime(2022, 3, 21)

        expected = (ps3, 120)
        actual = obter_orcamento_banhos(data, qt_pequenos=4, qt_grandes=2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()