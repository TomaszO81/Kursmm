#typy zmiennych
int
numer =23

dobule
waga = 85.5

#sringi imutable nie zmienna

imie ="magda"


#bool
true
false
#indeksowanie

imie[2]

#do dlugosci
len(imie)

imie[len(imie)-1]

# silicing

imie[0:9:2]
imie[0::2]
imie[::2]


#odworcenie stringa
imie[::-1]

imie.format()

"moje imie {}".format(imie)

#operatory
dodawanie i odejmowanie moznenie dzielne rownsc przypisanie modulo
=,-,+=, -= *,**,/,// %

#boolean
True
False

and or not

True and True = True
True nad False =False

True or True = True

False or True = True


not True or True = True

not (True or True) = False

instrukcje do sterowania programem

if True:
   pass
   #to rob cos

elif True:
    pass
    #jezli pierwszy jest nie prawdziwy

else:tylko jeden musi byc

if 6 > 5:
    print("LOL")


#pętle
for i in range (1000):
print("ola")

i=0
while i < 10000:
    print("ola")
    i += 1

for each -- bardziej

brake - przerywa petle calkowicie
continue -- przerywa dla elementu ktory mam teraz

#listy
kolekcje danych , podmienac po indeksie,

lista1 = ["ola",1, [1,2, "osiem"]]
lista1[2]= "jeden"

lista1 [::]

x = lista1[3][1]  - odwlanie sie do listy w liscie  bedzie skopiowa po referencji deep coopy

dir(nazwa_modulu)  -- pomoc z konkrentgo modulu to help() wyswietli pomoc o modulu

# import copy
from import copy

from copy import  *

#funkcje

modolowy i przenosny

def funkcja():
    pass

#1
def funkcja1(imie, nazwisko ="kowlaski"):
    print(imie, nazwisko)

    argumenty sa obowiazkowe i domyslne, kolejnosc jest wazna


def star_wars(name):
    return "Jedi {}".format(name)

arek_jedi = star_wars("tomek")


def star_wars1(name):
    jedi = star_wars("tomek")
    return "Jedi {}".format(name)

print(jedi)


def star_wars1(name):
    """
    Trenuje kandydatk jedi
    :param name:
    :return:
    """
    global arek_jedi
    arek_jedi = star_wars("tomek")
    return arek_jedi


#pliki
file = open('path', 'r')

with open('file.csv' , 'w') as plik:
    tresc =plik.read()

plik.seek(23)

plik.writelines()

#try wyjatek

plik = None

try:

except klika razy
    finally: tylko raz

try:
    open("plik.txt" 'r') as plik:
        plik.read()
  except Exception:
    print("blad i tyle")
finlly:

#slowniki
klucze unikalne
nie powtarzalne

slownik = {1:"ola", 'dwa':3}

x = slownik[1]

y = slownik['dwa']

slownik.update({'nowy':[1,2,3,4,5]})

print(slownik)

slownik.keys()
slownik.values()

krotka_tuple = 1,2,2,

#kopoiowanie  -- to ponizej powinno byc w innym pliku
def deepcopy(wyraz):
    return str(wyraz).capitalize()

print((deepcopy("ola w module kopia")))
-----
from kopia import deepcopy

print(deepcopy)



