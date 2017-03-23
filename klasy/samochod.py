class Samochod(object):
    def __init__(self, marka, kolor): #metoda kontruktor
        self.producent = marka
        self.kolor = kolor
        self.czy_jedzie = False
        self.silnik = None


    def zatrab(self, intesywnosc):
        if intesywnosc > 10:
         return 'piiiiiiiii'
        else:
         return 'pi'

    def jedz(self):
        self.czy_jedzie = True

    def zatrzymaj(self):
        self.czy_jedzie = False




