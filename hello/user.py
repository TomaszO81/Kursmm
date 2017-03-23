imie = input("Podaj imię ")
# wpythonie 3.6 mozna tak
#print(f"Witaj {imie}!") # f-do formatowania
#print("witaj "+imie)

imie = imie.capitalize()
print("Witaj {}".format(imie))

x = imie.find('A')
print(x)