from pojazd import Pojazd
from rower import Rower
from rower_dziec import Dzieciey
from samochod import Samochod

poj1 = Pojazd('ogolny')

print(poj1)

rower1 = Rower('Romet')
print(rower1)
print(rower1.zadzown())
print(rower1.kola)
print(rower1.jedz())
print('-------------')
dzieciecy1 = Dzieciey()
print(dzieciecy1.nazwa)
print(dzieciecy1.kola)
#dzieciecy2 = Dzieciey

print(rower1.jedz())
#print(dzieciecy2.jedz())

auto1 = Samochod('Volvo')
print(auto1)
auto1.moc = 163
auto1.tuning()
print(auto1.moc)


auto2 = Samochod('BMW')
auto2.moc = 180
print(auto1 > auto2)
