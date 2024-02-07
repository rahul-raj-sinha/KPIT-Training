
class Animal:

    def eat(self):
        print("animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Birds fly......")

class Chicken(Bird):

    def disp(self):
        print("Chickens are breeded for consumption.....")

chick = Chicken()
chick.disp()
chick.fly()
chick.eat()
