class Pojazd(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.kola = None

    def jedz(self):
        return 'Jedzie'

    def stop(self):
        return 'Zatrzymany'

    def __str__(self):
        return 'Pojazd {}'.format(self.nazwa)
