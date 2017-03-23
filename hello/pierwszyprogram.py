imie = input("Podaj swoje imie ?")
nazwisko = input("Podaj swoje nazwisko ?")
wzrost = input("Podaj swoj wzrost ?")
wiek = input ("Podaj swoj wiek ?")
rok_ur = 2017 - int(wiek)


print("Witaj {}".format(imie))
print("Witaj {}".format(nazwisko))
print("Twoj wzrost w centymetrach to {:.2f}".format(float(wzrost)))
print("Twoj rok urodzenia to {} lat".format(rok_ur))

#print("Witaj {} {}, masz {} lat! oraz {} wzrostu".format(imie,nazwisko,wiek))