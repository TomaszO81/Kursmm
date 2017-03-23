name = str(input("Podaj imie: "))

# jesli ostania litera konczy sie na litere 'a' to najprawdopodbniej kobieta

if name.endswith("a") and not name == "Jan Maria":
    print("Hej {}, jesteś najprawodopodbnie kobietą".format(name))

# jezeli napisze Jan Maria Rokita to witamy Rokita
elif name == "Jan Maria":
    print("Witaj Panie  Rokita")


else:
    print("Hej {} jestes mezczyzna".format(name))