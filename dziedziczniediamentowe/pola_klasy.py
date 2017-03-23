#pola klasy
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


    def __str__(self):
        return ('{} stanowisko: {}'.format(self.imie, self.stanowisko))

    #def __del__(self):


pracaownik1 = Pracownik('John Turturo', 'aktor')
pracaownik2 = Pracownik('John Travolta', 'Gwiazda')

pracaownik1.set_pay(5000)
pracaownik2.set_pay(8000)

print(pracaownik1)
print(pracaownik2)
print(pracaownik1.liczba_pracownikow)
print(Pracownik.liczba_pracownikow)
print(pracaownik2.liczba_pracownikow)

print('pwysokosc podzywki')
print(Pracownik.roczna_podwyzka)
print(pracaownik1.roczna_podwyzka)
print(pracaownik2.roczna_podwyzka)

print('pwysokosc podzywki')
Pracownik.roczna_podwyzka = 8
print(Pracownik.roczna_podwyzka)
print(pracaownik1.roczna_podwyzka)
print(pracaownik2.roczna_podwyzka)

print(Pracownik.__dict__)
print(pracaownik1.__dict__)
print(pracaownik2.__dict__)
print('zmiwniamy wysokosc podwyzki w 1 instakcji')
pracaownik2.roczna_podwyzka = 12
print(Pracownik.roczna_podwyzka)
print(pracaownik1.roczna_podwyzka)
print(pracaownik2.roczna_podwyzka)

print(Pracownik.__dict__)
print(pracaownik1.__dict__)
print(pracaownik2.__dict__)