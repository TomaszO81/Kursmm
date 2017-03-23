#po podaniu nazwy miesisaca
#program napisze ilosc dni w miesiacu

# styczen, luty...

miesiac = input("Podaj miesiac: ")

# czy to jest  luty
if miesiac == "luty":
    print("Luty ma 28 lub 29 dni")



# czy to jest miesiac ktory ma 31 dni
elif miesiac == "styczen" or miesiac == "marzec":
    print("{} ma 31 dni".format(miesiac))
# czy to miesiac ktory ma 30 dni


#nie ma takiego miesiaca

#PEP 8 python