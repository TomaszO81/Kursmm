from pojazd import Pojazd


class Rower(Pojazd):
    def __init__(self, nazwa):
        Pojazd.__init__(self, nazwa)
        Pojazd.kola = 2



    def zadzown(self):
        return 'dryn dryn'