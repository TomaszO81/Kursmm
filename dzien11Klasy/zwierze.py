class Zwierze(object):
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return '{} ma {} lat'.format(self.imie,self.wiek)

    def powiedz(self):
        print('Zwierze nie mowi')


zwierz1 = Zwierze('Mucha', 1)
print(zwierz1)


class Kot(Zwierze):
    def powiedz(self):
        print('mial mial')

class Pies(Zwierze):
    def powiedz(self):
        print("hau hau")

    def merdaj(self):
        print('Ogon lata')


class Czlowiek(Zwierze):
    def powiedz(self):
        print("Czesc")

class Student(Czlowiek):
    def powiedz(self):
        return Zwierze.powiedz(self)
        print("poprosze troje")



kot1 = Kot('Filemon',2)
print(kot1)
kot1.powiedz()

pies1 = Pies('Reksio', 5)
print(pies1)
print(issubclass(Pies, Zwierze))
pies1.powiedz()
pies1.merdaj()

studen1 = Student("janek",20)
studen1.powiedz()
