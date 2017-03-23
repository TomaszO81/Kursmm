#obliczamy czy podany rok jest przestepny
#podzilny przez 4, nie podzielny przez 100 ale podzielny przez 400


# rok = str(input("Podaj rok"))
#
# if rok.isdigit() and int(rok) !=0:
#
# #if dane.isdigit():
#     liczba = int(rok)
#
#    #sprawdzamy czy podzielna przez 3
#     if liczba % 4 == 0 :
#         #napisz ze podzielna przez 3
#         print("Rok {} jest podzielny przez 4".format(liczba))
#
#

rok = str(input("Podaj rok"))

if rok % 400 == 0:
    print("Jest przestepny")
elif rok % 4 == 0 and rok % 100 != 0:
    print("Jest przestepny")
else:
    print("Nie jest przestepny")