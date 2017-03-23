# Sprawdzić czy podana fraza jest polingrom "KAJAK"

#input fraza od uztkownika

#sprawdzamy czy jest palingramem

  #jesli fraza == fraza odwrotna to jest OK  _-> przeksztalcic stringa
  #else NO

# import zad1
#
# odwrocony = zad1.odwroc("arek")
#
# print(odwrocony)

from zad1 import odwroc

fraza = input("Podaj wyrażenie: ")

if fraza == odwroc(fraza):
    print("{} jest panidromem".format(fraza))
else:
    print("{} nie jest palindormem:".format(fraza))
