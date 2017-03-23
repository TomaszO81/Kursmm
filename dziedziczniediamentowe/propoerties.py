class Pracownik(object):
    def __init__(self, imie, nazwisko, stanowisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__stanowisko = stanowisko


    def wypisz_imie(self):
        print(self.__imie)

    @property
    def stanowisko(self):
        if self.__stanowisko != None:
            return  str(self.__stanowisko).capitalize()

    @stanowisko.setter
    def stanowisko(self, nazwa):
        if str(nazwa).isalpha():
          self.__stanowisko = nazwa

    @stanowisko.deleter
    def stanowisko(self):
        self.__stanowisko = None
        print('Usowam stanowisko')




pra1 = Pracownik('Jan', 'Kowlaski', 'aktor')
print(pra1.stanowisko)


pra1.stanowisko = 'gwiazda'
print(pra1.stanowisko)

del pra1.stanowisko
print(pra1.__dict__)