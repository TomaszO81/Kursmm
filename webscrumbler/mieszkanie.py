import requests
from bs4 import BeautifulSoup
from ogloszenie import Ogloszenie
import pickle


ogloszenia = []
adres = 'https://www.otodom.pl/wynajem/mieszkanie/gdansk/oliwa/?search%5Bdescription%5D=1&search%5Bdist%5D=0&search%5Bdistrict_id%5D=16&search%5Border%5D=created_at_first%3Adesc&nrAdsPerPage=72'

res = requests.get(adres)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

ads = soup.select('.offer-item-header a')
#print(ads)
#print(res.text)

for ad in ads:

    o = Ogloszenie(ad.getText(), ad.get('href'))
    print(o.opis)
    print(o.link)
    ogloszenia.append(o)
   #komentuje ale tylko jenorazowo Ogloszenie.zapisz_ogloszenia('ogloszenia.dat', ogloszenia)
ogloszenia_plik = Ogloszenie.wczytaj_ogloszenia('ogloszenia.dat')
for o in ogloszenia_plik:
    print(o.opis, o.link)

    # print(ad)
    # print(ad.getText())
    # print(ad.get('href'))
    # print('------------------')

