# zwroc liste bez duplikatow

lista =[10,20,30,20,10,50,50,40,80,50,40]

lista_bez_duplikatow = []

for element in lista:
    if element not in lista_bez_duplikatow:
        lista_bez_duplikatow.append(element)

print(lista_bez_duplikatow)

