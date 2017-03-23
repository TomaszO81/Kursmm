wynik = 3
lista_a = ["zero", "jeden", wynik]
print("Lista a:" , lista_a)


wynik = 43
print("Lista a zmian wynik:", lista_a)

lista_b = lista_a.copy()
print("lista b:", lista_b)

lista_a.append("new element")

print("lista a:", lista_a)
print("lista b:", lista_b)