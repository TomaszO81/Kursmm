from unittest import TestCase
from pracownik import Pracownik
from test_helper import Helper

class PracownikTesty(TestCase):

    def setUp(self):
        imie = 'Jan'
        nazwisko = 'Kowalaski'
        self.p = Pracownik(imie, nazwisko)


    def tearDown(self):
        pass



    def test_konstruktor(self):
        self.assertIsNotNone(self.p)


    def test_stanowisko_get(self):
        self.p.stanowisko = 'aktor'
        self.assertEqual(self.p.stanowisko, 'Aktor')


    def test_nazwisko_get(self):
        self.assertEqual(self.p.nazwisko_get(), str('Kowalaski').upper())

    def test_wypisz_imie(self):
        funkcja_testowana = self.p.wypisz_imie

        otrzymany_outoput = Helper.get_print_output(funkcja_testowana)
        oczekiwany_out = self.imie + '\n'

        self.assertEqual(otrzymany_outoput, oczekiwany_out)


