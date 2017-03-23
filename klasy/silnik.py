class Silnik(object):
    def __init__(self, moc, pojemnosc):
        '''
        Tworzy instancje Silnika
        :param moc:
        :param pojemnosc:
        '''
        self.horse_power = moc
        self.volume = pojemnosc
        self.pracuje = False
        self.stop = False

    def uruchom(self):
        self.pracuje =True

    def zatrzymaj(self):
        self.stop = True