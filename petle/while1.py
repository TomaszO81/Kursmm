# x =True
#
# while x:
#     print(x)
#     x = False

# name = 'Joanna'
#
# i = 0
#
# while i < len(name):
#     print(name[i])
#     i += 1
#
# print("Ostania instrukcja")
#
# #pythontutor.com

# przyjmij haslo od uzytkownika
password = input("Podaj hasło: ")

# dopoki haslo nie spelni warunkow
while (not len(password) > 6) :

   #napisz ze zle haslo
   if len(password) < 4:
       print("Bardzo słabe hasło")

   else:
       print("Słabe hasło")

   #przyjmij znowu haslo
   password = input("Podaj hasło, min 6 znaków: ")


#podziekuj za podanie prawidlowego hasla
print("Prawidlowe haslo")


