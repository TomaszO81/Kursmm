from samochod import Samochod

#inclilizujemy obiekt
#tworzymy instancje klasy klasy samochod


auto1 = Samochod('Volvo', 'czarny')
auto2 = Samochod('Tesla', 'niebieski')
print(auto1.producent, auto1.kolor)
#print(auto2.producent, auto2.kolor)

auto1.zatrab(5)

print(auto2.producent, auto2.zatrab(11))

auto1.jedz()
print(auto1.czy_jedzie)

