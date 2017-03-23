# tryb w zapisuje do pliku i go tworzy tryb a tez zapisuje do pliku na koncu lini i zapisuje tyb w zapisuje

with open('mojplik.txt', 'r+') as plik:

    plik.seek(len(plik))