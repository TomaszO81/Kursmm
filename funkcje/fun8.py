def dodaj_imie(imie, imiona=None):
    if imiona is None:
        imiona = []
        imiona.append(imie)
        return imiona

print(dodaj_imie("ola"))
print(dodaj_imie("ala"))

