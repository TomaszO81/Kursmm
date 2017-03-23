from pojazd import Pojazd


class Samochod(Pojazd):
    def __init__(self, marka):
        Pojazd.__init__(self, marka)
        self.kola = 4
        self.moc = None

    def tuning(self):
        self.moc += 30

    def __gt__(self, other):
        return self.moc > other.moc

    def __str__(self):
        return 'Samochod marki {}'.format(self.nazwa)
