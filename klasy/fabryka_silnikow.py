import silnik
from samochod import Samochod

maly_silnik = silnik.Silnik(75,1000)
sredni_silnik = silnik.Silnik(160, 1600)
V8 = silnik.Silnik(400, 5000)

#print(V8.horse_power)
#print(maly_silnik.horse_power)

volvo = Samochod('volvo', 'black')

volvo.silnik = sredni_silnik

print(volvo.silnik.horse_power)

audi = Samochod('audi', 'srebrny')
audi.silnik = maly_silnik

print('audi ma silnik o mocy {}'.format(audi.silnik.horse_power))

print(audi.silnik.pracuje)
audi.silnik.uruchom()

print(audi.silnik.pracuje)

print(audi.silnik.stop)