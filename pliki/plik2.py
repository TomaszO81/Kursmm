# otwieramy sobie plik

plik = open('mojplik.txt', 'r')

print(plik.readline())

print(plik.tell())

print(plik.readline())
print(plik.readline())
plik.close()