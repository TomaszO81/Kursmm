class Animal(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print('Say nothiong')

    def __str__(self):
        return  str(self.name).capitalize()


class Horse(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def say(self):
        print('Hej jestem koń')

    def jump(self):
        print("kon skacze")

class Donkey(Animal):
    def say(self):
        print('ihmmm jestem osiol')

    def run(self):
        print('ja nie biegam jestem oslem')


class Mule(Horse, Donkey):
    def say(self):
        print('Jestem mułem')



animal = Animal('zwierzak')
print(animal)

kon1 = Horse('Kary')
print(kon1)
kon1.say()
kon1.jump()

osial1 = Donkey('donkey kong')
osial1.say()
osial1.run()

mul1 = Mule('Mułek')
mul1.say()
mul1.jump()