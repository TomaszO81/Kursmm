class Ogloszenie(object):

    def __init__(self, opis, link):
        self.opis = self.__formatuj_opis(opis)
        self.link = link

    def __formatuj_opis(self, opis):
        o = str(opis).split('\n')
        return ' '.join(o).strip()

    @staticmethod
    def zapisz_ogloszenia(nazwa_pliku, lista):
        import pickle
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(lista, plik)

    @staticmethod
    def wczytaj_ogloszenia(nazwa_pliku):
        import pickle
        with open(nazwa_pliku, 'rb') as plik:
            return pickle.load(plik, encoding='utf-8')
