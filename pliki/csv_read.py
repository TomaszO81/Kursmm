
baza_osob = []

with open('osoby.txt', 'r') as plik:
    opisy_kolumn = plik.readline()
    for line in plik:

        line = line.strip()

        osoba = line.split(',')

        osoba[2] = int(osoba[2])

        print(osoba)

        baza_osob.append(osoba)


print()
print(baza_osob)