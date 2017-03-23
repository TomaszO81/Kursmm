import shutil, os, send2trash

# #print(shutil.disk_usage(/Users/tomek/Documents)
#
# print(os.getcwd())
# os.chdir('//Users//tomek//Documents')
# print(os.getcwd())
# os.mkdir('/Users/tomek/Documents/Tomek2')
# print(os.getcwd())
#
# shutil.move()
# shutil.copytree('C:\\asds', 'C:\\asd')
#
# os.unlink('C:\\dzien8\\pre\\aas')
#
# os.shutil.rmtree('C:\\dzien8\\')
#
# send2trash.send2trash('Users/tomek/Documents/Tomek2')

# for folder_aktulany, podfolder, pliki in os.walk('/Users/tomek/PycharmProjects/day3/'):
#     print('Obecny folder to:', folder_aktulany)
#
#     for podkatalog in podfolder:
#         print('SUBFOLDER wew. {} : {}'.format(folder_aktulany,podkatalog))
#
#         for plik in pliki:
#             print('Plik wew. folder {} , {}'.format(folder_aktulany,plik))
#     print()
#
# dir = os.path.abspath('/day3/')
# print(dir)

fotki = '/Users/tomek/Documents/Foto'
for inkdes, plik in enumerate(os.listdir(fotki)):
    # print('fotka {} : inkdes {}'.format(plik,inkdes))
    stary_plik = os.path.join(fotki,plik)
    print(stary_plik)

    root ='wakacje'
    nazwa_pliku, ext = os.path.splitext(plik)

    nowa_nazwa = root + '_' + str(inkdes) + ext
    nowy_plik = os.path.join(fotki, nowa_nazwa)

    #print(nowy_plik)
    shutil.move(stary_plik, nowy_plik)

    #print('{} : {:>30} {} - {}')