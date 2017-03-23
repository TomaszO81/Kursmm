# usowanie elementów z listy

lista = ["kwiatek", "doniczka", "ziemia", "woda"]

#x = lista.pop(-2)
#lista.remove("doniczka")

#print(lista)

#lista.remove("doniczka")
#print(lista)1

element_usuwany = "doniczka"

if element_usuwany in lista:
    lista.remove(element_usuwany)
else:
    print("Nie ma takiego elementu")

print(lista)

