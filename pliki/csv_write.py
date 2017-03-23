osoba = ['arek', 'gutkowski', 30]


with open('osoby.txt', 'a') as plik:

    for element in osoba:
        plik.write(str(element)+ ',')