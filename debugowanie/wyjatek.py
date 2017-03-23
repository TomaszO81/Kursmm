naglowek =''

try:

    with open('dane.csv', 'r') as plik:
         naglowek = plik.readline()

except FileNotFoundError:
    print("Nie znaleziono pliku")

print('Nagłowek: {}'.format(naglowek))