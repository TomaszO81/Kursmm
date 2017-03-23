#
# plik = open('mojplik.txt')
#
# tresc = plik.read(21)
# print(plik.tell())
#
# print(tresc)
#
# plik.close()


plik = open('mojplik.txt')

print("To jest pierwsza linijka: ")
print(plik.readline(), 'end=')

tresc = plik.read()
print("read() odczyta od drugiej linijki")
print(tresc)
print(plik.tell())
plik.close()