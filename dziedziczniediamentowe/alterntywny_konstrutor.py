#metody klasy
class Pracownik(object):

    liczba_pracownikow = 0
    roczna_podwyzka = 5

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1

    def set_pay(self, amount):
        self.pay = amount

    def daj_roczna_podwyzka(self):
        self.pay += self.pay * (1/self.roczna_podwyzka)

    @classmethod
    def okles_rocz_podw(cls, wartosc):
        if wartosc > 8:
           cls.roczna_podwyzka = 8
        else:
            cls.roczna_podwyzka = wartosc


    @classmethod
    def z_pensja(cls, imie, stanowisko, pensja):
        cls.pensja = pensja
        return cls(imie, stanowisko)


os1 = Pracownik.z_pensja('Jan', 'aktor', 5000)
print(os1)

print(os1.pay)
print(os1.imie)

os2 = Pracownik.z_pensja('Janina', 'aktorka', 3000)

print(os2.pay)
print(os2.imie)



