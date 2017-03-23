
with open('mojplik.txt', 'r') as plik:
    #print(len(plik.read())# )
    text = plik.read()
    print(len(text))

    print(ord(text[-1]))


