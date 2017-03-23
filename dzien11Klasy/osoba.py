class Osoba(object):

    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.wiek = None

    def __str__(self):
        return "{}, {}, ma pesel{}".format(self.imie,self.nazwisko,self.pesel)

    def __add__(self, other):
        return self.wiek + other.wiek

czlowiek1 = Osoba('jan', 'kowlaski', '81231231232')
czlowiek1.wiek = 30

czlowiek2 = Osoba('Mateusz', 'Nowak', '234234234234')
czlowiek2.wiek =34

print(czlowiek1)
print(czlowiek1+czlowiek2)

# print(czlowiek1.imie)
# print(czlowiek1.nazwisko)
# print(czlowiek1.pesel)