# oblicz ilosc liczb dla danego zakresu liczb parzystych i nieparzystych

zakres = range(0, 100)
parzysta = 0
nieparzysta = 0

for liczba in zakres:
    # jesli przysta to  dodać do licznika przystych
    if liczba % 2 == 0:
        parzysta += 1
    else:
        nieparzysta += 1

print("Parzyste: {}, nieparzyste: {}".format(parzysta,nieparzysta))