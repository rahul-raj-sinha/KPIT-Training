
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("animals eat......")

    def fun(self):
        print("Hello World..... Animal")

class Person:

    def __init__(self):
        print("Person Ctor....")
        self.p = 20

    def talk(self):
        print("person talks")

    def fun(self):
        print("Hello World..... Person")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor.....")
        self.g = 30



gracy = Girl()
gracy.eat()
gracy.talk()
gracy.fun()


print("-" * 60)
print(gracy.__dict__)
