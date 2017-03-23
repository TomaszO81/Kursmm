from rower import Rower


class Dzieciey(Rower):
    def __init__(self):
        self.nazwa = 'dzieciecy'
        Rower.__init__(self, self.nazwa)
        self.kola = 4

    def jedz(self):
        return 'Jedzie wolno'

