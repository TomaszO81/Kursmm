#zamiana temperatury
# wejscie: "35C"  "100F"
# wyjscie: "Temperatura w {typ} tp {xxx} stopni"
# C = (F - 32)  * (5/9)
# F = C * (9/5) + 32


temp = str(input("Podaj temperaturę: ")).upper()

if temp.endswith("C"):

    cel =temp[:-1]
    cel = int(cel)

    farh =  cel * (9/5) + 32
    print("Temperatura w Farenhaitah to {} stopni".format(farh))


# sprawdzamy ostani znak
# jesli C
  # obliczamy F
  # wypisujemy
elif temp.endswith("F"):
    farh = int(temp[0:-1])

    cel = (farh -32) * 5/9

#jesli F
  #obliczamy C
  #wypisujemy
    print("Temperatura w Celciusza to {} stopni".format(cel))

