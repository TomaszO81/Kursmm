#fizz buzz  wypisz liczby od 1 do 100 wlacznie
#/3 =>fizz jesli podzielna przez 3 to wypisz FIZZ
#/5 =>buzz jesli podzielna przez 5 to wypisz BUZZZ
#/3 /5 Fizz buzz jelsi podzielan przez 3 i 5


#licznik

i = 1
# petla
#dopoki liczby mniejsze rowne 100:
while i <= 100:

    #jesli licznik podielna przez 15

        if i % 15 == 0:
            print('FIZZBUZZ')

        # napisz FIZZ BIZZ
        elif i % 3 == 0:
            print('FIZZ')

        # jesli liczba podzielna przez 3
            # napisz FIZZ

        elif i % 5 == 0:
           print('BUZZ')


        #jesli licznik podzielna przez 5
            #napisz BIZZ
        else:
            print(i)

        # w innym przypadku
        # wypisz wartosc licznika
        i += 1


    # update licznika
