

slownik = {'klucz': 'wartość', 0:'jakos tam watosc klucza'}

print(len(slownik))

print(slownik[0])

for klucz, wartosc in slownik.items():
    print("klucz {}, wartosc {}".format(klucz,wartosc))


for klucz in slownik.keys():
    print(klucz)