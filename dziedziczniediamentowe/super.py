class Wielokat(object):
    def __init__(self, id):
        self.id = id

class Prostakat(Wielokat):
    def __init__(self, id, szerokosc, wysokosc):
        super().__init__(id)
        self.ksztalt = (szerokosc, wysokosc)

class Kwadrat(Prostakat):
    pass

prostokat1 = Prostakat ('A' , 30, 20)
print(prostokat1)

kwadrat1 = Kwadrat('B', 50 , 50)
print(kwadrat1)