

try:
    #w ith open('dane.csv', 'r') as plik:
        # linie = plik.readline()

    print("To jest kod bez bledu")

except FileNotFoundError:
    print("Nie ma pliku")

finally:
    print("To jest blok finally")