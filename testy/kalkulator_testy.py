from unittest import TestCase

import kalkulator

class KalkualtorTesty(TestCase):

    def test_add(self):
        wynik = kalkulator.add(2,3)
        self.assertEqual(wynik,5)

    def test_multi(self):
        wynik = kalkulator.multi(2,3)
        self.assertEqual(wynik,6)

    def test_divide(self):
        wynik = kalkulator.divide(2,3)
        self.assertAlmostEqual(wynik,0.6666,5)

#test
