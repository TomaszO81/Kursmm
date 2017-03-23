class Matematyka(object):
    @staticmethod
    def pole_prostokata(bok_a, bok_b):
        return bok_a * bok_b

pole = Matematyka.pole_prostokata(30, 40)
print('Pole wynosi', pole)