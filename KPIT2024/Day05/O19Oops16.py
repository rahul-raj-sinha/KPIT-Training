
class Animal:

    def eat(self):
        print("Animals eat...")


class Bird(Animal):

    def fly(self):
        print("Birds Fly.....")


class Chicken(Bird):

    def fun(self):
        print("Chicken's are breeded for consumption.......")

    def fly(self):
        print(f"Chickens seldom fly......")

chick = Chicken()
chick.fun()
chick.fly()
chick.eat()
